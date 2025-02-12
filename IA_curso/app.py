from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import joblib
from sklearn.metrics.pairwise import cosine_similarity

# Configuración de la base de datos
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///validaciones.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Cargar modelos y datos
modelo = joblib.load(r"C:\Users\santi\Desktop\Modelo\Modelos_entrenados\modelo_cups\modelo_cups_v2.pkl")
vectorizer = joblib.load(r"C:\Users\santi\Desktop\Modelo\Modelos_entrenados\modelo_cups\vectorizer_v2.pkl")
le = joblib.load(r"C:\Users\santi\Desktop\Modelo\Modelos_entrenados\modelo_cups\label_encoder_v2.pkl")

df = pd.read_excel(r"C:\Users\santi\Desktop\Modelo\Documentos_procesados\cups_procesado.xlsx")
df["Habilitado"] = df["Habilitado"].apply(lambda x: 1 if x == "SI" else 0)
df["UsoCodigoCUP_encoded"] = df["UsoCodigoCUP"].map({"AP": 1, "AC": 0})

# Crear una clase de modelo para la base de datos
class Validacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cups = db.Column(db.String(20), nullable=False)
    descripcion = db.Column(db.String(255), nullable=False)
    tipo_atencion = db.Column(db.String(2), nullable=False)
    resultado = db.Column(db.String(255), nullable=False)
    fecha = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<Validacion {self.id} - {self.cups}>'

def validar_cups(cups_ingresado, descripcion, tipo_atencion):
    if cups_ingresado not in df["Codigo"].values:
        desc_vectorizada = vectorizer.transform([descripcion]).toarray()
        desc_completa = vectorizer.transform(df["Nombre"]).toarray()
        similitudes = cosine_similarity(desc_vectorizada, desc_completa)
        idx_mas_similar = similitudes.argmax()
        cups_sugerido = df.iloc[idx_mas_similar]["Codigo"]
        descripcion_sugerida = df.iloc[idx_mas_similar]["Nombre"]
        tipo_atencion_sugerido = df.iloc[idx_mas_similar]["UsoCodigoCUP"]
        return f"❌ CUPS incorrecto. Sugerencia: Usa {cups_sugerido} - {descripcion_sugerida} ({tipo_atencion_sugerido})."

    datos_cups = df[df["Codigo"] == cups_ingresado].iloc[0]
    tipo_atencion_correcto = datos_cups["UsoCodigoCUP"]
    tipo_atencion_ingresado = 1 if tipo_atencion == "AP" else 0

    if tipo_atencion_ingresado != datos_cups["UsoCodigoCUP_encoded"]:
        tipo_correcto_text = "AP" if datos_cups["UsoCodigoCUP_encoded"] == 1 else "AC"
        ejemplo = df[df["UsoCodigoCUP_encoded"] == datos_cups["UsoCodigoCUP_encoded"]].iloc[0]
        return f"❌ Tipo de atención incorrecto. El CUPS {cups_ingresado} es para '{tipo_correcto_text}'. Ejemplo: Usa {ejemplo['Codigo']} - {ejemplo['Nombre']}."

    descripcion_correcta = datos_cups["Nombre"]
    desc_vectorizada = vectorizer.transform([descripcion]).toarray()
    desc_correcta_vectorizada = vectorizer.transform([descripcion_correcta]).toarray()
    similitud = cosine_similarity(desc_vectorizada, desc_correcta_vectorizada)[0][0]

    if similitud < 0.8:
        return f"❌ La descripción no coincide con el CUPS ingresado. El CUPS {cups_ingresado} corresponde a: '{descripcion_correcta}'."

    return "✅ El CUPS ingresado, la descripción y el tipo de atención son válidos."

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        cups = request.form['cups']
        descripcion = request.form['descripcion']
        tipo_atencion = request.form['tipo_atencion']
        fecha = request.form['fecha']  # Capturar la fecha seleccionada
        resultado = validar_cups(cups, descripcion, tipo_atencion)
        
        # Guardar los resultados en la base de datos
        validacion = Validacion(cups=cups, descripcion=descripcion, tipo_atencion=tipo_atencion,
                                resultado=resultado, fecha=fecha)
        db.session.add(validacion)
        db.session.commit()

    return render_template('index.html', resultado=resultado)

# Crear las tablas de la base de datos al inicio
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

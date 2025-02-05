import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics.pairwise import cosine_similarity
import joblib

# Cargar los datos
df = pd.read_excel("cups_procesado.xlsx")

# Convertir a valores binarios (1 = Sí, 0 = No)
df["Habilitado"] = df["Habilitado"].apply(lambda x: 1 if x == "SI" else 0)

# Codificar correctamente el tipo de atención
df["UsoCodigoCUP_encoded"] = df["UsoCodigoCUP"].map({"AP": 1, "AC": 0})

# Vectorizar la descripción
vectorizer = TfidfVectorizer(max_features=100)
X_desc = vectorizer.fit_transform(df["Nombre"]).toarray()

# Codificar los códigos CUPS a valores numéricos
le = LabelEncoder()
df["CUPS_encoded"] = le.fit_transform(df["Codigo"])

# Combinar las características
X = pd.concat([
    pd.DataFrame(X_desc),
    df[["UsoCodigoCUP_encoded", "Habilitado"]]
], axis=1)

X.columns = X.columns.astype(str)
y = df["CUPS_encoded"]

# Dividir los datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar el modelo
modelo = RandomForestClassifier(n_estimators=20, max_depth=10, random_state=42)
modelo.fit(X_train, y_train)

# Guardar modelos
joblib.dump(modelo, 'modelo_cups_v2.pkl', compress=3)
joblib.dump(vectorizer, 'vectorizer_v2.pkl', compress=3)
joblib.dump(le, 'label_encoder_v2.pkl', compress=3)


def validar_cups(cups_ingresado, descripcion, tipo_atencion):
    if cups_ingresado not in df["Codigo"].values:
        desc_vectorizada = vectorizer.transform([descripcion]).toarray()
        desc_completa = vectorizer.transform(df["Nombre"]).toarray()
        similitudes = cosine_similarity(desc_vectorizada, desc_completa)
        idx_mas_similar = similitudes.argmax()
        cups_sugerido = df.iloc[idx_mas_similar]["Codigo"]
        descripcion_sugerida = df.iloc[idx_mas_similar]["Nombre"]
        tipo_atencion_sugerido = df.iloc[idx_mas_similar]["UsoCodigoCUP"]
        return f"❌ CUPS incorrecto.\nSugerencia: Usa {cups_sugerido} - {descripcion_sugerida} ({tipo_atencion_sugerido})."

    datos_cups = df[df["Codigo"] == cups_ingresado].iloc[0]
    tipo_atencion_correcto = datos_cups["UsoCodigoCUP"]

    # Convertir `tipo_atencion` ingresado a su codificación
    tipo_atencion_ingresado = 1 if tipo_atencion == "AP" else 0

    if tipo_atencion_ingresado != datos_cups["UsoCodigoCUP_encoded"]:
        tipo_correcto_text = "AP" if datos_cups["UsoCodigoCUP_encoded"] == 1 else "AC"
        ejemplo = df[df["UsoCodigoCUP_encoded"] == datos_cups["UsoCodigoCUP_encoded"]].iloc[0]
        return f"❌ Tipo de atención incorrecto.\nEl CUPS {cups_ingresado} es para '{tipo_correcto_text}'.\nEjemplo: Usa {ejemplo['Codigo']} - {ejemplo['Nombre']}."

    # **Validación de la descripción**
    descripcion_correcta = datos_cups["Nombre"]
    desc_vectorizada = vectorizer.transform([descripcion]).toarray()
    desc_correcta_vectorizada = vectorizer.transform([descripcion_correcta]).toarray()
    similitud = cosine_similarity(desc_vectorizada, desc_correcta_vectorizada)[0][0]

    if similitud < 0.8:  # Umbral de similitud
        return f"❌ La descripción no coincide con el CUPS ingresado.\nEl CUPS {cups_ingresado} corresponde a: '{descripcion_correcta}'."

    return "✅ El CUPS ingresado, la descripción y el tipo de atención son válidos."

# Pruebas
print(validar_cups("010100", "PUNCIÓN CISTERNAL SOD", "AC"))  # Descripción incorrecta
print(validar_cups("010100", "PUNCION CISTERNAL SOD", "AC"))  # Datos correctos
print(validar_cups("890201", "CONSULTA DE PRIMERA VEZ POR MEDICINA GENERAL", "AP")) # datos correctos
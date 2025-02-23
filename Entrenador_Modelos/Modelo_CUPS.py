import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Cargar el archivo procesado de CIE10
df_cie10 = pd.read_excel(r"C:\Users\santi\Desktop\Modelo\Documentos_procesados\cie10_procesado.xlsx")

# Vectorizar la columna "Nombre_CIE10" con TF-IDF
vectorizer_cie10 = TfidfVectorizer(max_features=100)
X_desc_cie10 = vectorizer_cie10.fit_transform(df_cie10["Nombre_CIE10"]).toarray()

# Codificar los códigos CIE10 a valores numéricos
le_cie10 = LabelEncoder()
df_cie10["CIE10_encoded"] = le_cie10.fit_transform(df_cie10["Codigo_CIE10"])

# Construir la matriz de entrenamiento X
X_cie10 = pd.concat([
    pd.DataFrame(X_desc_cie10),
    df_cie10[["HabilitadoCIE10"]]
], axis=1)

X_cie10.columns = X_cie10.columns.astype(str)
y_cie10 = df_cie10["CIE10_encoded"]

# Dividir los datos en entrenamiento y prueba
X_train_cie10, X_test_cie10, y_train_cie10, y_test_cie10 = train_test_split(
    X_cie10, y_cie10, test_size=0.2, random_state=42
)

# Entrenar el modelo RandomForest
modelo_cie10 = RandomForestClassifier(n_estimators=20, max_depth=10, random_state=42)
modelo_cie10.fit(X_train_cie10, y_train_cie10)

# Guardar los modelos entrenados
joblib.dump(modelo_cie10, r"C:\Users\santi\Desktop\Modelo\Modelos_entrenados\modelo_cie10\modelo_cie10.pkl", compress=3)
joblib.dump(vectorizer_cie10, r"C:\Users\santi\Desktop\Modelo\Modelos_entrenados\modelo_cie10\vectorizer_cie10.pkl", compress=3)
joblib.dump(le_cie10, r"C:\Users\santi\Desktop\Modelo\Modelos_entrenados\modelo_cie10\label_encoder_cie10.pkl", compress=3)

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
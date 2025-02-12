import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics.pairwise import cosine_similarity
import joblib
import re

# Cargar el archivo procesado de CIE10
df_cie10 = pd.read_excel(r"C:\Users\santi\Desktop\Modelo\Documentos_procesados\cie10_procesado.xlsx")

# Función para limpiar texto manteniendo puntuación
def limpiar_texto(texto):
    if isinstance(texto, str):
        return re.sub(r'\s+', ' ', texto.strip()).lower()
    return ""

# Aplicar limpieza a columnas relevantes
df_cie10["Nombre_CIE10"] = df_cie10["Nombre_CIE10"].apply(limpiar_texto)
df_cie10["Descripcio_CIE10"] = df_cie10["Descripcio_CIE10"].apply(limpiar_texto)
df_cie10["Codigo_CIE10"] = df_cie10["Codigo_CIE10"].astype(str).str.strip()

# Cargar el vectorizador guardado o reentrenarlo con más palabras
try:
    vectorizer_cie10 = joblib.load(r"C:\Users\santi\Desktop\Modelo\Modelos_entrenados\modelo_cie10\vectorizer_cie10.pkl")
  
except:
    vectorizer_cie10 = TfidfVectorizer(max_features=None)  # Aumentar el límite de palabras reconocidas
    X_desc_cie10 = vectorizer_cie10.fit_transform(df_cie10["Nombre_CIE10"]).toarray()
    joblib.dump(vectorizer_cie10, r"C:\Users\santi\Desktop\Modelo\Modelos_entrenados\modelo_cie10\vectorizer_cie10.pkl", compress=3)
    print("✅ Vectorizador entrenado y guardado con más términos.")

# Codificar los códigos CIE10 a valores numéricos
le_cie10 = LabelEncoder()
df_cie10["CIE10_encoded"] = le_cie10.fit_transform(df_cie10["Codigo_CIE10"])

# Construir la matriz de entrenamiento X
X_desc_cie10 = vectorizer_cie10.transform(df_cie10["Nombre_CIE10"]).toarray()
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
joblib.dump(le_cie10, r"C:\Users\santi\Desktop\Modelo\Modelos_entrenados\modelo_cie10\label_encoder_cie10.pkl", compress=3)


# Función de validación con depuración de vectorización
def validar_cie10(codigo_ingresado, nombre, descripcion):
    codigo_ingresado = codigo_ingresado.strip()
    nombre = limpiar_texto(nombre)
    descripcion = limpiar_texto(descripcion)
    
   
    if codigo_ingresado not in df_cie10["Codigo_CIE10"].values:
        return f"❌ Código CIE10 incorrecto. No se encontró en la base de datos. Código ingresado: {codigo_ingresado}"
    
    datos_cie10 = df_cie10[df_cie10["Codigo_CIE10"] == codigo_ingresado].iloc[0]
    nombre_correcto = datos_cie10["Nombre_CIE10"]
    descripcion_correcta = datos_cie10["Descripcio_CIE10"]
    
    similitud_nombre = cosine_similarity(
        vectorizer_cie10.transform([nombre]).toarray(), 
        vectorizer_cie10.transform([nombre_correcto]).toarray()
    )[0][0]
    similitud_descripcion = cosine_similarity(
        vectorizer_cie10.transform([descripcion]).toarray(), 
        vectorizer_cie10.transform([descripcion_correcta]).toarray()
    )[0][0]
    

    
    if similitud_nombre < 0.65:
        return f"❌ El nombre no coincide con el código CIE10 ingresado.\nNombre esperado: '{nombre_correcto}'\nNombre ingresado: '{nombre}'"
    
    if similitud_descripcion < 0.65:
        return f"❌ La descripción no coincide con el código CIE10 ingresado.\nDescripción esperada: '{descripcion_correcta}'\nDescripción ingresada: '{descripcion}'"
    
    return "✅ El código CIE10 ingresado, el nombre y la descripción son válidos."


print(validar_cie10("A000", "COLERA DEBIDO A VIBRIO CHOLERAE 01", "COLERA"))  # ✅ Correcto
print(validar_cie10("A031", "SHIGELOSIS DEBIDA A SHIGELLA FLEXNERI", "SHIGELOSIS"))  # ✅ Correcto
print(validar_cie10("123", "FIEBRE TIFOIDEA", "FIEBRES TIFOIDEA Y PARATIFOIDEA"))  # ❌ Código incorrecto con sugerencia
print(validar_cie10("A010", "123", "FIEBRES TIFOIDEA Y PARATIFOIDEA"))  # ❌ Nombre incorrecto
print(validar_cie10("A010", "FIEBRE TIFOIDEA", "123"))  # ❌ Descripción incorrecta
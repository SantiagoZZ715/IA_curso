# Importamos las librerías necesarias
import pandas as pd  # Para manejar datos en formato de tabla (DataFrame)
import numpy as np  # Para operaciones numéricas
import re  # Para limpiar el texto con expresiones regulares
import string  # Para eliminar signos de puntuación
from sklearn.model_selection import train_test_split  # Para dividir los datos en entrenamiento y prueba
from sklearn.feature_extraction.text import TfidfVectorizer  # Para convertir texto en números (TF-IDF)
from sklearn.linear_model import LogisticRegression  # Modelo de regresión logística
from sklearn.metrics import accuracy_score, classification_report  # Para evaluar el modelo

# -------------------------------
# 1. CREACIÓN DEL CONJUNTO DE DATOS
# -------------------------------
# Creamos un dataset de ejemplo con correos electrónicos y su clasificación (spam o no spam)
data = {
    "mensaje": [
        "¡Gana dinero rápido! Haz clic en este enlace ahora.",  # SPAM
        "Querido usuario, tu cuenta ha sido bloqueada. Ingresa aquí.",  # SPAM
        "Hola Juan, ¿quieres almorzar mañana?",  # NO SPAM
        "Oferta especial: Compra uno y llévate otro GRATIS.",  # SPAM
        "Confirmación de tu cita médica para el jueves.",  # NO SPAM
        "Haz clic aquí para reclamar tu premio sorpresa.",  # SPAM
        "Reunión de equipo programada para el viernes a las 10 AM.",  # NO SPAM
        "Hola mamá, llego a casa en 10 minutos."  # NO SPAM
    ],
    "etiqueta": [1, 1, 0, 1, 0, 1, 0, 0]  # 1 = Spam, 0 = No spam
}

# Convertimos los datos en un DataFrame de pandas
df = pd.DataFrame(data)

# -------------------------------
# 2. PREPROCESAMIENTO DEL TEXTO
# -------------------------------
# Creamos una función para limpiar los correos electrónicos
def limpiar_texto(texto):
    texto = texto.lower()  # Convertimos el texto a minúsculas
    texto = re.sub(f"[{string.punctuation}]", "", texto)  # Eliminamos signos de puntuación
    texto = re.sub(r"\d+", "", texto)  # Eliminamos números
    return texto

# Aplicamos la limpieza a todos los mensajes del dataset
df["mensaje"] = df["mensaje"].apply(limpiar_texto)

# -------------------------------
# 3. DIVISIÓN DE LOS DATOS (ENTRENAMIENTO Y PRUEBA)
# -------------------------------
# Separamos los datos en conjuntos de entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(df["mensaje"], df["etiqueta"], test_size=0.2, random_state=42)

# -------------------------------
# 4. CONVERSIÓN DE TEXTO A NÚMEROS (TF-IDF)
# -------------------------------
# TF-IDF (Term Frequency - Inverse Document Frequency) convierte el texto en vectores numéricos
# TF: Frecuencia de una palabra en un documento
# IDF: Cuánto aporta una palabra para distinguir documentos (reduce el peso de palabras comunes)
vectorizer = TfidfVectorizer()

# Ajustamos y transformamos los datos de entrenamiento con TF-IDF
X_train_tfidf = vectorizer.fit_transform(X_train)

# Solo transformamos los datos de prueba (usamos el mismo vectorizador)
X_test_tfidf = vectorizer.transform(X_test)

# -------------------------------
# 5. ENTRENAMIENTO DEL MODELO DE REGRESIÓN LOGÍSTICA
# -------------------------------
# Regresión logística: Modelo de clasificación binaria que usa una función sigmoide
modelo = LogisticRegression()
modelo.fit(X_train_tfidf, y_train)  # Entrenamos el modelo con los datos procesados

# -------------------------------
# 6. EVALUACIÓN DEL MODELO
# -------------------------------
# Hacemos predicciones en los datos de prueba
y_pred = modelo.predict(X_test_tfidf)

# Medimos la precisión del modelo
print("Precisión del modelo:", accuracy_score(y_test, y_pred))

# Mostramos un reporte detallado con métricas de evaluación
print("Reporte de clasificación:\n", classification_report(y_test, y_pred))

# -------------------------------
# 7. PRUEBA CON NUEVOS MENSAJES
# -------------------------------
# Ahora probamos el modelo con nuevos correos
nuevos_mensajes = [
    "Te ganaste un viaje GRATIS, reclama aquí",  # SPAM (debería predecir 1)
    "Nos vemos mañana en la oficina"  # NO SPAM (debería predecir 0)
]

# Aplicamos la misma limpieza de texto
nuevos_mensajes_tfidf = vectorizer.transform([limpiar_texto(m) for m in nuevos_mensajes])

# Hacemos la predicción con el modelo entrenado
predicciones = modelo.predict(nuevos_mensajes_tfidf)

# Mostramos los resultados
for mensaje, pred in zip(nuevos_mensajes, predicciones):
    print(f"Mensaje: {mensaje} → {'SPAM' if pred == 1 else 'NO SPAM'}")

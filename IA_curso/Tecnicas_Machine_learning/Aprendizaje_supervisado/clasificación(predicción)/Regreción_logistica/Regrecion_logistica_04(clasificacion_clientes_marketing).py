# Importar las librerías necesarias
import pandas as pd  # Para manejar los datos
import numpy as np  # Para operaciones numéricas
from sklearn.model_selection import train_test_split  # Para dividir los datos
from sklearn.preprocessing import StandardScaler  # Para normalizar los datos
from sklearn.linear_model import LogisticRegression  # Modelo de regresión logística
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report  # Para evaluar el modelo

# -------------------------------
# 1. SIMULACIÓN DE UN CONJUNTO DE DATOS (para fines demostrativos)
# -------------------------------
# Crear un conjunto de datos simulado de clientes con características ficticias
data = {
    "Edad": [25, 45, 35, 50, 23, 41, 63, 52, 35, 40],  # Edad del cliente
    "Ingreso": [30000, 60000, 40000, 70000, 25000, 45000, 80000, 65000, 37000, 55000],  # Ingreso del cliente
    "Nivel_Educacion": [1, 3, 2, 3, 1, 2, 3, 3, 2, 2],  # Nivel de educación (1: Primaria, 2: Secundaria, 3: Universitario)
    "Historial_Compras": [5, 20, 8, 15, 3, 12, 25, 18, 7, 10],  # Número de compras anteriores
    "Promocion": [1, 0, 0, 1, 0, 1, 1, 1, 0, 1],  # 1: Recibió promoción, 0: No recibió promoción
    "Respuesta_Campaña": [1, 0, 0, 1, 0, 1, 1, 1, 0, 1]  # 1: Comprará, 0: No comprará
}

df = pd.DataFrame(data)

# -------------------------------
# 2. PREPROCESAMIENTO DE LOS DATOS
# -------------------------------
# Separar las características (X) y la variable objetivo (y)
X = df.drop("Respuesta_Campaña", axis=1)
y = df["Respuesta_Campaña"]

# Normalizar las características para que tengan la misma escala
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# -------------------------------
# 3. DIVISIÓN DE DATOS EN CONJUNTOS DE ENTRENAMIENTO Y PRUEBA
# -------------------------------
# Dividir los datos en un 80% para entrenamiento y 20% para prueba
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# -------------------------------
# 4. CREACIÓN Y ENTRENAMIENTO DEL MODELO DE REGRESIÓN LOGÍSTICA
# -------------------------------
# Instanciar el modelo de regresión logística
modelo = LogisticRegression()

# Entrenar el modelo con los datos de entrenamiento
modelo.fit(X_train, y_train)

# -------------------------------
# 5. EVALUACIÓN DEL MODELO
# -------------------------------
# Realizar predicciones sobre los datos de prueba
y_pred = modelo.predict(X_test)

# Evaluación del rendimiento del modelo
print("Precisión del modelo:", accuracy_score(y_test, y_pred))
print("\nReporte de clasificación:\n", classification_report(y_test, y_pred))

# Mostrar la matriz de confusión
print("\nMatriz de Confusión:\n", confusion_matrix(y_test, y_pred))

# -------------------------------
# 6. PRUEBA CON NUEVOS CLIENTES
# -------------------------------
# Datos de nuevos clientes para predecir si comprarán o no
nuevos_clientes = np.array([
    [30, 50000, 3, 12, 1],  # Cliente 1
    [60, 70000, 2, 15, 0],  # Cliente 2
    [25, 30000, 1, 5, 1],   # Cliente 3
])

# Normalizar los nuevos clientes utilizando el mismo escalador
nuevos_clientes_scaled = scaler.transform(nuevos_clientes)

# Predecir si los nuevos clientes comprarán o no
predicciones = modelo.predict(nuevos_clientes_scaled)

# Mostrar las predicciones
for i, pred in enumerate(predicciones):
    print(f"Cliente {i + 1} - {'Comprará' if pred == 1 else 'No Comprará'}")

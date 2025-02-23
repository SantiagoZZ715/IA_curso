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
# Crear un conjunto de datos simulado de pacientes con características ficticias
data = {
    "Glucosa": [120, 150, 180, 160, 95, 110, 220, 85, 145, 90],  # Nivel de glucosa en sangre
    "Presion_Arterial": [130, 140, 160, 155, 120, 125, 170, 115, 135, 110],  # Presión arterial
    "Frecuencia_Cardiaca": [80, 85, 90, 78, 70, 72, 95, 68, 88, 74],  # Frecuencia cardíaca
    "Edad": [45, 50, 60, 55, 35, 40, 65, 30, 50, 28],  # Edad
    "Antecedentes_Familiares": [1, 1, 1, 1, 0, 0, 1, 0, 1, 0],  # 1: antecedentes familiares de enfermedades, 0: no
    "Enfermedad": [1, 1, 1, 1, 0, 0, 1, 0, 0, 0]  # 1: tiene la enfermedad, 0: no la tiene
}

df = pd.DataFrame(data)

# -------------------------------
# 2. PREPROCESAMIENTO DE LOS DATOS
# -------------------------------
# Separar las características (X) y la variable objetivo (y)
X = df.drop("Enfermedad", axis=1)
y = df["Enfermedad"]

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
# 6. PRUEBA CON NUEVOS PACIENTES
# -------------------------------
# Datos de nuevos pacientes para predecir si tienen la enfermedad (1) o no (0)
nuevos_pacientes = np.array([
    [130, 140, 85, 48, 1],  # Paciente 1 (Posible enfermo)
    [95, 120, 72, 29, 0],   # Paciente 2 (No enfermo)
    [160, 155, 90, 60, 1],  # Paciente 3 (Posible enfermo)
])

# Normalizar los nuevos pacientes utilizando el mismo escalador
nuevos_pacientes_scaled = scaler.transform(nuevos_pacientes)

# Predecir si los nuevos pacientes tienen la enfermedad (1) o no (0)
predicciones = modelo.predict(nuevos_pacientes_scaled)

# Mostrar las predicciones
for i, pred in enumerate(predicciones):
    print(f"Paciente {i + 1} - {'Enfermedad' if pred == 1 else 'No Enfermedad'}")

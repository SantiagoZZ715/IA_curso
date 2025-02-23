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
# Crear un conjunto de datos simulado de transacciones con características ficticias
data = {
    "Monto_Compra": [100, 2000, 50, 500, 1500, 200, 10000, 300, 80, 150],
    "Ubicacion": [1, 3, 1, 2, 3, 1, 2, 1, 3, 2],  # 1: Local, 2: Internacional, 3: Online
    "Frecuencia_Compra": [5, 2, 10, 6, 1, 8, 1, 3, 12, 7],
    "Hora_Compra": [14, 3, 18, 10, 23, 12, 1, 16, 22, 19],  # Hora en formato de 24 horas
    "Fraude": [0, 1, 0, 0, 1, 0, 1, 0, 0, 0]  # 1: Fraude, 0: No Fraude
}

df = pd.DataFrame(data)

# -------------------------------
# 2. PREPROCESAMIENTO DE LOS DATOS
# -------------------------------
# Separar las características (X) y la variable objetivo (y)
X = df.drop("Fraude", axis=1)
y = df["Fraude"]

# Normalizar las características para que tengan la misma escala (importantísimo para algunos modelos)
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
# 6. PRUEBA CON NUEVAS TRANSACCIONES
# -------------------------------
# Datos de nuevas transacciones para predecir si son fraude o no
nuevas_transacciones = np.array([
    [120, 1, 5, 13],  # Transacción legítima
    [2500, 3, 1, 2],  # Posible fraude
    [60, 1, 7, 22],   # Transacción legítima
])

# Normalizar las nuevas transacciones utilizando el mismo escalador
nuevas_transacciones_scaled = scaler.transform(nuevas_transacciones)

# Predecir si las nuevas transacciones son fraude (1) o no (0)
predicciones = modelo.predict(nuevas_transacciones_scaled)

# Mostrar las predicciones
for i, pred in enumerate(predicciones):
    print(f"Transacción {i + 1} - {'Fraude' if pred == 1 else 'No Fraude'}")

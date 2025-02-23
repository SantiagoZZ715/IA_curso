import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.datasets import load_iris

# Cargar el dataset Iris desde Scikit-Learn
iris = load_iris()

# Convertirlo en un DataFrame de Pandas para facilidad de manipulación
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target  # Agregar la columna de etiquetas de las especies

# Mostrar las primeras filas del dataset
print(df.head())

X = df.iloc[:, :-1].values  # Características (4 columnas)
y = df.iloc[:, -1].values   # Etiquetas (0, 1, 2)

encoder = OneHotEncoder(sparse_output=False)
y = encoder.fit_transform(y.reshape(-1, 1))  # Convertir a matriz de 3 columnas (una por especie)

scaler = StandardScaler()
X = scaler.fit_transform(X)  # Normalización para mejorar el entrenamiento

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Definir el modelo MLP
model = keras.Sequential([
    keras.layers.Dense(10, activation='relu', input_shape=(4,)),  # Capa oculta 1
    keras.layers.Dense(8, activation='relu'),  # Capa oculta 2
    keras.layers.Dense(3, activation='softmax')  # Capa de salida con 3 neuronas (una por clase)
])

# Compilar el modelo
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Mostrar la estructura del modelo
model.summary()

history = model.fit(X_train, y_train, epochs=50, batch_size=5, validation_data=(X_test, y_test))

# Evaluar la precisión en los datos de prueba
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f'Precisión en datos de prueba: {test_acc:.4f}')

# Graficar la pérdida y la precisión
plt.figure(figsize=(12, 4))

# Pérdida
plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], label='Entrenamiento')
plt.plot(history.history['val_loss'], label='Validación')
plt.xlabel('Épocas')
plt.ylabel('Pérdida')
plt.legend()
plt.title('Evolución de la Pérdida')

# Precisión
plt.subplot(1, 2, 2)
plt.plot(history.history['accuracy'], label='Entrenamiento')
plt.plot(history.history['val_accuracy'], label='Validación')
plt.xlabel('Épocas')
plt.ylabel('Precisión')
plt.legend()
plt.title('Evolución de la Precisión')

plt.show()

# Hacer una predicción con una muestra de prueba
sample = X_test[0].reshape(1, -1)  # Tomamos una sola muestra y ajustamos la forma
prediction = model.predict(sample)
predicted_class = np.argmax(prediction)  # Obtener la clase con mayor probabilidad

print(f'Predicción: {iris.target_names[predicted_class]}')

model.save("modelo_iris.h5")

modelo_cargado = keras.models.load_model("modelo_iris.h5")


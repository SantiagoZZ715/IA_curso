import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

# Cargar el dataset MNIST desde Keras
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Normalizar los datos (convertimos los valores de píxeles de 0-255 a 0-1)
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

# Aplanar las imágenes 28x28 a vectores de 784 características
x_train = x_train.reshape(-1, 28*28)
x_test = x_test.reshape(-1, 28*28)

# Convertir etiquetas a one-hot encoding
y_train = keras.utils.to_categorical(y_train, 10)
y_test = keras.utils.to_categorical(y_test, 10)

def build_model(activation_function):
    model = keras.Sequential([
        keras.layers.Dense(128, activation=activation_function, input_shape=(784,)),  # Capa oculta 1
        keras.layers.Dense(64, activation=activation_function),  # Capa oculta 2
        keras.layers.Dense(10, activation='softmax')  # Capa de salida con 10 neuronas (una por dígito)
    ])
    
    # Compilar el modelo
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    
    return model

activations = ["relu", "sigmoid", "tanh"]
histories = {}

for activation in activations:
    print(f"\nEntrenando modelo con activación: {activation}")
    model = build_model(activation)
    history = model.fit(x_train, y_train, epochs=10, batch_size=32, validation_data=(x_test, y_test), verbose=1)
    
    # Guardar el historial del entrenamiento
    histories[activation] = history

    plt.figure(figsize=(12, 6))

for activation in activations:
    plt.plot(histories[activation].history['val_accuracy'], label=f"Activación: {activation}")

plt.xlabel("Épocas")
plt.ylabel("Precisión en Validación")
plt.legend()
plt.title("Comparación de Funciones de Activación - Precisión en Validación")
plt.show()



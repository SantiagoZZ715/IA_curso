import tensorflow as tf
import keras
import numpy as np
import matplotlib.pyplot as plt

# Cargar el conjunto de datos MNIST directamente desde Keras
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Mostrar la forma de los datos
print(f"Train images shape: {x_train.shape}")  # (60000, 28, 28)
print(f"Test images shape: {x_test.shape}")    # (10000, 28, 28)

# Mostrar algunas imágenes con sus etiquetas
fig, axes = plt.subplots(1, 5, figsize=(10, 3))
for i, ax in enumerate(axes):
    ax.imshow(x_train[i], cmap='gray')
    ax.set_title(f"Dígito: {y_train[i]}")
    ax.axis('off')
plt.show()

# Normalizar los valores de los píxeles al rango [0, 1]
x_train = x_train / 255.0
x_test = x_test / 255.0

# Aplanar las imágenes 28x28 a un vector de 784 valores
x_train = x_train.reshape(-1, 28 * 28)
x_test = x_test.reshape(-1, 28 * 28)

# Convertir las etiquetas a formato one-hot encoding
y_train = keras.utils.to_categorical(y_train, 10)
y_test = keras.utils.to_categorical(y_test, 10)

# Definir la arquitectura de la red neuronal
model = keras.Sequential([
    keras.layers.Dense(128, activation='relu', input_shape=(784,)),  # Capa oculta 1
    keras.layers.Dense(128, activation='relu'),  # Capa oculta 2
    keras.layers.Dense(10, activation='softmax')  # Capa de salida
])

# Compilar el modelo
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Mostrar la estructura del modelo
model.summary()

# Entrenar el modelo con los datos de entrenamiento
history = model.fit(x_train, y_train, epochs=10, batch_size=32, validation_data=(x_test, y_test))

# Evaluar el modelo con los datos de prueba
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f'Precisión en datos de prueba: {test_acc:.4f}')

# Hacer una predicción sobre las primeras 5 imágenes del conjunto de prueba
predictions = model.predict(x_test[:5])

# Mostrar las imágenes con sus predicciones
fig, axes = plt.subplots(1, 5, figsize=(10, 3))
for i, ax in enumerate(axes):
    ax.imshow(x_test[i].reshape(28, 28), cmap='gray')
    ax.set_title(f"Pred: {np.argmax(predictions[i])}")
    ax.axis('off')
plt.show()

model.save("modelo_mnist.h5")

modelo_cargado = keras.models.load_model("modelo_mnist.h5")



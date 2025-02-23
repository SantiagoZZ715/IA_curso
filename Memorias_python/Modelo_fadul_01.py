import tensorflow as tf  # Librería para crear y entrenar redes neuronales
import numpy as np  # Manejo de arreglos numéricos eficientes
import matplotlib.pyplot as plt  # Visualización de gráficos

# Definir los datos de entrada y salida
celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)  # Temperaturas en grados Celsius
fahrenheit = np.array([-40, 14, 32, 46.4, 59, 71.6, 100.4], dtype=float)  # Temperaturas equivalentes en Fahrenheit

# Crear el modelo de red neuronal
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])  # Capa densa con una sola neurona y una entrada
])

# Compilar el modelo
model.compile(
    loss='mean_squared_error',  # Función de pérdida: error cuadrático medio (MSE)
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.1)  # Optimizador Adam con tasa de aprendizaje de 0.1
)

# Entrenar el modelo con los datos de entrenamiento
history = model.fit(celsius, fahrenheit, epochs=1000, verbose=False)  # 1000 épocas, sin imprimir detalles

# Función para convertir Celsius a Fahrenheit usando el modelo entrenado
def celsius_to_fahrenheit(celsius_input):
    celsius_input = np.array([[celsius_input]], dtype=float)  # Convertir la entrada en un array bidimensional
    return model.predict(celsius_input)[0][0]  # Hacer la predicción y devolver el valor resultante

# Pedir al usuario una temperatura en Celsius y convertirla a Fahrenheit
try:
    user_celsius = float(input("Enter temperature in Celsius: "))  # Obtener entrada del usuario
    fahrenheit_result = celsius_to_fahrenheit(user_celsius)  # Calcular la temperatura en Fahrenheit
    print(f"{user_celsius} degrees Celsius is equal to {fahrenheit_result:.2f} degrees Fahrenheit.")  # Mostrar resultado
except ValueError:
    print("Please enter a valid numeric value.")  # Manejar error si la entrada no es numérica

# Graficar la evolución del error durante el entrenamiento
plt.xlabel('Epoch Number')  # Etiqueta del eje X
plt.ylabel("Loss Magnitude")  # Etiqueta del eje Y
plt.plot(history.history['loss'])  # Graficar la pérdida a lo largo de las épocas
plt.title("Model Training Loss")  # Título del gráfico
plt.show()  # Mostrar la gráfica

# Declaramos una variable y le asignamos un valor entero
edad = 25  
print(edad)  # Imprime el valor de la variable edad

# Inicializamos una variable con un valor
nombre = "Juan"  
print(nombre)  # Imprime "Juan"

# Reasignamos un nuevo valor a la misma variable
nombre = "Carlos"  
print(nombre)  # Imprime "Carlos"

# Entero
numero = 10  

# Decimal (float)
pi = 3.1416  

# Cadena de texto (string)
mensaje = "Hola, mundo"  

# Booleano (True o False)
es_mayor = True  

print(numero, pi, mensaje, es_mayor)  # Imprime los valores de todas las variables

# Definimos dos variables de tipo string
saludo = "Hola"
nombre = "Ana"

# Concatenamos usando el operador +
frase = saludo + ", " + nombre + "!"  
print(frase)  # Imprime "Hola, Ana!"

# Definimos dos variables numéricas
a = 10
b = 5

# Realizamos operaciones matemáticas
suma = a + b  # Suma
resta = a - b  # Resta
multiplicacion = a * b  # Multiplicación
division = a / b  # División (devuelve un float)

print(suma, resta, multiplicacion, division)  # Imprime los resultados

# Definimos una función que usa una variable global
def saludar():
    mensaje = "¡Bienvenido!"  # Variable local dentro de la función
    print(mensaje)

saludar()  # Llamamos a la función para imprimir el mensaje

# Convertimos un número en cadena
numero = 100
texto = str(numero)  # Convertimos el número en string
print(texto, type(texto))  # Imprime "100" y <class 'str'>

# Convertimos una cadena en número
cadena_numero = "50"
numero_entero = int(cadena_numero)  # Convertimos la cadena en entero
print(numero_entero, type(numero_entero))  # Imprime 50 y <class 'int'>

# Creamos una lista con diferentes elementos
frutas = ["Manzana", "Banana", "Cereza"]

# Accedemos a un elemento de la lista usando su índice
print(frutas[1])  # Imprime "Banana"

# Modificamos un elemento de la lista
frutas[0] = "Pera"
print(frutas)  # Imprime ['Pera', 'Banana', 'Cereza']

# Creamos un diccionario con información de una persona
persona = {
    "nombre": "Luis",
    "edad": 30,
    "ciudad": "Madrid"
}

# Accedemos a los valores del diccionario usando sus claves
print(persona["nombre"])  # Imprime "Luis"
print(persona["edad"])  # Imprime 30

# Modificamos un valor en el diccionario
persona["edad"] = 31
print(persona["edad"])  # Imprime 31

# Definimos una variable con un número
numero = 10

# Usamos una estructura condicional para evaluar la variable
if numero > 5:
    print("El número es mayor que 5")
else:
    print("El número es menor o igual a 5")

# Usamos la variable en un bucle
contador = 1
while contador <= 3:
    print("Iteración:", contador)
    contador += 1  # Incrementamos el contador

    
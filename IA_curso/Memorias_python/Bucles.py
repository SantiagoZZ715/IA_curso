"""
Los bucles son estructuras de control de flujo que permiten ejecutar un bloque de código repetidamente mientras se cumpla 
una condición determinada. Son muy útiles cuando queremos realizar una tarea repetitiva, 
como iterar sobre elementos en una lista o realizar una acción múltiples veces sin tener que escribir el mismo código una
 y otra vez.
"""

#recorriendo una lista con for

colores = ["rojo", "verde", "azul"]

for color in colores:
    print(f"Color: {color}")

#recorre un rango de numeros con range 

for num in range(1, 6):
    print(num)

#repetir hasta que una condición se cumpla
contador = 0

while contador < 5:
    print(f"Contador: {contador}")
    contador += 1

#recorrer una cadena de texto

palabra = "Python"

for letra in palabra:
    print(letra)+

#sumar elementos de una lista

numeros = [1, 2, 3, 4, 5]
suma = 0

for num in numeros:
    suma += num

print(f"Suma total: {suma}")

# solciitar datos al usuario hasta que se cumpla una condición
entrada = ""

while entrada.lower() != "salir":
    entrada = input("Escribe algo (o 'salir' para terminar): ")
    print(f"Escribiste: {entrada}")

# recorrer claves y valores de un diccionario

persona = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}

for clave, valor in persona.items():
    print(f"{clave}: {valor}")

#interrumpir un bucle cuando se cumpla una condición

for num in range(10):
    if num == 5:
        break
    print(num)

#saltar una iteración

for num in range(5):
    if num == 3:
        continue
    print(num)

#multiplicar valores de una lista

numeros = [1, 2, 3, 4]
dobles = [num * 2 for num in numeros]

print(dobles)

#recorriendo una matriz

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for fila in matriz:
    for num in fila:
        print(num, end=" ")
    print()

#calcular el factorial de un número 

n = 5
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"Factorial de {n}: {factorial}")

# ejemplo de impresión con for

for i in range(1, 6):
    print("*" * i)

#encontrar el numero mayor en una lista

numeros = [10, 5, 20, 8]
mayor = numeros[0]

for num in numeros:
    if num > mayor:
        mayor = num

print(f"Número mayor: {mayor}")

# contar elementos en una lista

numeros = [1, 2, 3, 4, 5]
contador = 0

for _ in numeros:
    contador += 1

print(f"Cantidad de elementos: {contador}")

#convertir una lista de int a string

numeros = [1, 2, 3, 4]
strings = [str(num) for num in numeros]

print(strings)

#filtrar numeros pares en una lista

numeros = [1, 2, 3, 4, 5, 6]
pares = [num for num in numeros if num % 2 == 0]

print(pares)

#generar secuencia de fibonnaci

n = 10
a, b = 0, 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

#recorrer una tupla con fir

dias = ("Lunes", "Martes", "Miércoles")

for dia in dias:
    print(dia)

#ejecución de codigo al terminar un blucle

for i in range(3):
    print(i)
else:
    print("Bucle terminado")

"""
match-case es una estructura de control introducida en Python 3.10 que permite manejar múltiples casos de forma similar a switch-case en otros lenguajes como C, Java o JavaScript.

Se usa para comparar una variable con diferentes patrones y ejecutar el código correspondiente al primer caso coincidente.

Menú interactivo con while y match-case
Permite al usuario seleccionar una opción hasta que decida salir
"""

while True:
    print("\nMenú:")
    print("1. Saludar")
    print("2. Despedirse")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    match opcion:
        case "1":
            print("¡Hola!")
        case "2":
            print("¡Adiós!")
        case "3":
            print("Saliendo...")
            break
        case _:
            print("Opción no válida, intenta de nuevo.")

"""
Calculadora simple con while
Realiza operaciones matemáticas hasta que el usuario decida salir.
"""

while True:
    print("\nCalculadora:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    match opcion:
        case "1" | "2":
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))

            match opcion:
                case "1":
                    print(f"Resultado: {num1 + num2}")
                case "2":
                    print(f"Resultado: {num1 - num2}")
        case "3":
            print("Saliendo...")
            break
        case _:
            print("Opción inválida.")

"""
Juego de adivinanza con while
El usuario debe adivinar el número secreto.
"""

import random

numero_secreto = random.randint(1, 10)

while True:
    intento = int(input("Adivina el número (1-10): "))

    match intento:
        case _ if intento < numero_secreto:
            print("Demasiado bajo.")
        case _ if intento > numero_secreto:
            print("Demasiado alto.")
        case _:
            print("¡Correcto!")
            break

"""
Validar contraseña con while
El usuario debe ingresar la contraseña correcta.
"""

contraseña_correcta = "python123"

while True:
    contraseña = input("Ingresa la contraseña: ")

    match contraseña:
        case "python123":
            print("Contraseña correcta, acceso permitido.")
            break
        case _:
            print("Contraseña incorrecta, intenta de nuevo.")


"""
Contador con while y match
El usuario puede incrementar, decrementar o salir.
"""

contador = 0

while True:
    print(f"\nValor actual: {contador}")
    print("1. Incrementar")
    print("2. Decrementar")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    match opcion:
        case "1":
            contador += 1
        case "2":
            contador -= 1
        case "3":
            print("Saliendo...")
            break
        case _:
            print("Opción no válida.")

"""
Convertir temperaturas con while y match
El usuario puede convertir entre Celsius y Fahrenheit.
"""
while True:
    print("\nConversor de temperatura:")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    match opcion:
        case "1":
            celsius = float(input("Ingresa grados Celsius: "))
            print(f"{celsius}°C = {(celsius * 9/5) + 32}°F")
        case "2":
            fahrenheit = float(input("Ingresa grados Fahrenheit: "))
            print(f"{fahrenheit}°F = {(fahrenheit - 32) * 5/9}°C")
        case "3":
            print("Saliendo...")
            break
        case _:
            print("Opción no válida.")

"""
Convertir números a texto
El usuario ingresa un número y se muestra en palabras.
"""
while True:
    numero = input("Ingresa un número del 1 al 5 (o 'salir'): ")

    match numero:
        case "1":
            print("Uno")
        case "2":
            print("Dos")
        case "3":
            print("Tres")
        case "4":
            print("Cuatro")
        case "5":
            print("Cinco")
        case "salir":
            print("Adiós.")
            break
        case _:
            print("Número no reconocido.")

"""
Contador con límite
Cuenta hasta un número ingresado por el usuario.
"""

limite = int(input("Ingresa el número límite: "))
contador = 0

while contador <= limite:
    match contador:
        case _ if contador % 2 == 0:
            print(f"{contador} es par.")
        case _:
            print(f"{contador} es impar.")

    contador += 1

"""
Juego de piedra, papel o tijera
El usuario juega contra la computadora.
"""

import random

opciones = ["piedra", "papel", "tijera"]

while True:
    usuario = input("Elige piedra, papel o tijera (o 'salir'): ").lower()
    computadora = random.choice(opciones)

    match usuario:
        case "salir":
            print("Juego terminado.")
            break
        case "piedra" | "papel" | "tijera":
            print(f"La computadora eligió: {computadora}")
            match (usuario, computadora):
                case (u, c) if u == c:
                    print("Empate.")
                case ("piedra", "tijera") | ("papel", "piedra") | ("tijera", "papel"):
                    print("Ganaste.")
                case _:
                    print("Perdiste.")
        case _:
            print("Opción inválida.")

"""
Contar vocales en una frase
Cuenta cuántas vocales hay en una frase.
"""

frase = input("Escribe una frase: ").lower()
contador = 0
i = 0

while i < len(frase):
    match frase[i]:
        case "a" | "e" | "i" | "o" | "u":
            contador += 1
    i += 1

print(f"Número de vocales: {contador}")

contador = 1  # Inicializamos una variable con valor 1

while contador <= 5:  # La condición es que contador sea menor o igual a 5
    print(f"El contador está en: {contador}")  # Se imprime el valor actual del contador
    contador += 1  # Se incrementa el contador en 1 en cada iteración

print("Fin del ciclo.")

contraseña_correcta = "python123"
contraseña_ingresada = ""  # Variable vacía para iniciar el ciclo

while contraseña_ingresada != contraseña_correcta:  # Mientras no sea correcta, sigue pidiendo
    contraseña_ingresada = input("Ingrese la contraseña: ")

print("¡Acceso concedido!")

import random

numero_secreto = random.randint(1, 10)  # Genera un número aleatorio entre 1 y 10
intento = 0  # Inicializamos la variable intento

while intento != numero_secreto:  # Mientras el intento no sea correcto, seguimos pidiendo
    intento = int(input("Adivina el número (1-10): "))

print("¡Felicidades! Adivinaste el número.")


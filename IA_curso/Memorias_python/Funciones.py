"""
Una función en Python es un bloque de código reutilizable que se utiliza para realizar una tarea específica.
 Una vez que defines una función, puedes invocarla (llamarla) tantas veces como sea necesario,
   lo que hace que tu código sea más modular y fácil de leer y mantener.

Las funciones pueden aceptar entradas (parámetros o argumentos) y pueden devolver un valor 
(aunque también pueden no devolver nada). Las funciones permiten organizar el código de manera que, al hacer cambios,
 no necesites modificar el programa completo, sino solo la función correspondiente.
"""


"""
Función simple (def)
Definición:
Una función en Python se define con def, y se ejecuta cuando se la llama.
"""

def saludar():
    print("¡Hola, bienvenido!")

saludar()  # Llamada a la función

"""
Función con parámetros
Definición:
Permite recibir valores como entrada y usarlos dentro de la función.
"""

def saludar(nombre):
    print(f"¡Hola, {nombre}!")

saludar("Carlos")

"""
Función con valor de retorno (return)
Definición:
Devuelve un valor para ser usado más adelante.
"""

def suma(a, b):
    return a + b

resultado = suma(5, 3)
print("La suma es:", resultado)

"""
Función con valores por defecto
Definición:
Si un argumento no es proporcionado, se usa un valor predeterminado.
"""

def presentar(nombre, edad=18):
    print(f"Nombre: {nombre}, Edad: {edad}")

presentar("Ana")  # Usa el valor predeterminado (18)
presentar("Luis", 25)  # Usa el valor 25

"""
Función con múltiples argumentos (*args)
Definición:
Permite recibir una cantidad variable de argumentos.
*args almacena todos los valores como una tupla.
"""

def sumar_todo(*numeros):
    return sum(numeros)

print(sumar_todo(1, 2, 3, 4, 5))  # 15
print(sumar_todo(10, 20))  # 30

"""
Función con argumentos clave (**kwargs)
Definición:
Permite recibir argumentos con nombre en forma de diccionario.
**kwargs almacena los argumentos como un diccionario {clave: valor}.
"""

def mostrar_info(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Carlos", edad=30, ciudad="Madrid")

"""
Función lambda (Funciones anónimas)
Definición:
Funciones cortas de una sola línea.
"""

doble = lambda x: x * 2

print(doble(5))  # 10

"""
Función dentro de otra función (Funciones anidadas)
Definición:
Una función dentro de otra.
"""

def operacion(a, b):
    def suma():
        return a + b
    return suma()

print(operacion(4, 6))  # 10

"""
 Función como argumento de otra función
Definición:
Las funciones pueden pasarse como parámetros.
"""

def cuadrado(n):
    return n * n

def aplicar_funcion(func, valor):
    return func(valor)

print(aplicar_funcion(cuadrado, 4))  # 16

"""
Función recursiva
Definición:
Se llama a sí misma para resolver problemas repetitivos como el cálculo del factorial.
"""

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120

"""
Resumen de Tipos de Funciones

Función simple	             Ejecuta código cuando se la llama.
Con parámetros	             Recibe valores de entrada.
Con return	                 Devuelve un valor para su uso posterior.
Con valores por defecto	     Usa valores predeterminados si no se proporcionan.
Con *args	                 Acepta una cantidad variable de argumentos posicionales.
Con **kwargs	             Acepta una cantidad variable de argumentos con clave-valor.
Lambda (anónima)	         Función corta de una sola línea.
Anidada	                     Definida dentro de otra función.
Como argumento	             Puede pasarse como parámetro a otra función.
Recursiva	                 Se llama a sí misma para resolver problemas repetitivos.
"""
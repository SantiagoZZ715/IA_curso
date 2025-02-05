"""
Los tipos de datos en Python definen la naturaleza de los valores que pueden ser almacenados en las variables.
Cada tipo de dato tiene características específicas que determinan cómo se pueden manipular
y qué operaciones se pueden realizar sobre ellos.

Python es un lenguaje dinámicamente tipado,
lo que significa que no necesitas declarar el tipo de una variable al momento de crearla.
Python lo infiere automáticamente según el valor que se le asigne.
"""

numero1 = 42  # Número entero positivo
numero2 = -7  # Número entero negativo
numero3 = 1000000  # Número entero grande

print(type(numero1), type(numero2), type(numero3))  # <class 'int'>

decimal1 = 3.14  # Número decimal
decimal2 = -2.718  # Número decimal negativo
decimal3 = 1.2e3  # Notación científica (equivale a 1200.0)

print(type(decimal1), type(decimal2), type(decimal3))  # <class 'float'>

texto1 = "Hola, mundo"  # Comillas dobles
texto2 = 'Python es genial'  # Comillas simples
texto3 = """Esto es un texto
en múltiples líneas"""  # Comillas triples

print(type(texto1), type(texto2), type(texto3))  # <class 'str'>

es_verdadero = True  # Valor booleano verdadero
es_falso = False  # Valor booleano falso
comparacion = (10 > 5)  # Devuelve True

print(type(es_verdadero), type(es_falso), type(comparacion))  # <class 'bool'>

#estructura ordenada que peude contener cualquier tipo de dato

lista1 = [1, 2, 3, 4, 5]  # Lista de enteros
lista2 = ["manzana", "banana", "cereza"]  # Lista de strings
lista3 = [10, "Python", 3.14, True]  # Lista mixta

print(type(lista1), type(lista2), type(lista3))  # <class 'list'>

#similares a las listar pero inmutables no se modifican sus datos despues de la creación

tupla1 = (1, 2, 3, 4, 5)  # Tupla de enteros
tupla2 = ("rojo", "verde", "azul")  # Tupla de strings
tupla3 = (True, 3.14, "Hola")  # Tupla mixta

print(type(tupla1), type(tupla2), type(tupla3))  # <class 'tuple'>

#colecciones desordenadas de elementos unicos

conjunto1 = {1, 2, 3, 4, 5}  # Conjunto de enteros
conjunto2 = {"a", "b", "c", "a"}  # Conjunto de caracteres (los repetidos se eliminan)
conjunto3 = {True, False, True, False}  # Conjunto booleano

print(type(conjunto1), type(conjunto2), type(conjunto3))  # <class 'set'>

#estructura de clase valor

diccionario1 = {"nombre": "Ana", "edad": 25}  # Diccionario con datos personales
diccionario2 = {"Python": 1991, "JavaScript": 1995}  # Diccionario con lenguajes y su año de creación
diccionario3 = {1: "uno", 2: "dos", 3: "tres"}  # Diccionario con claves numéricas

print(type(diccionario1), type(diccionario2), type(diccionario3))  # <class 'dict'>

#representa la ausencia del valor

valor_nulo1 = None  # Variable sin valor asignado
valor_nulo2 = print("Hola")  # print devuelve None
valor_nulo3 = None if False else None  # Expresión que devuelve None

print(type(valor_nulo1), type(valor_nulo2), type(valor_nulo3))  # <class 'NoneType'>

"""
1. Listas (list)
Cuándo usarlas:
Cuando necesitas almacenar múltiples elementos en un orden específico.
Cuando los elementos pueden cambiar (agregar, eliminar o modificar).
Para recorrer secuencias con bucles (for o while).
"""

# Lista de nombres
nombres = ["Ana", "Carlos", "Luis", "María"]

# Accediendo a elementos por índice
print(nombres[1])  # Carlos

# Modificando un elemento
nombres[2] = "Pedro"

# Agregando un nuevo elemento
nombres.append("Sofía")

# Eliminando un elemento
nombres.remove("Ana")

# Iterando la lista
for nombre in nombres:
    print(nombre)

"""
2. Tuplas (tuple)
Cuándo usarlas:
Cuando los datos no deben cambiar después de su creación.
Para representar estructuras fijas, como coordenadas (x, y), fechas (año, mes, día), etc.
Cuando quieres mejorar el rendimiento (las tuplas son más rápidas que las listas).
"""

# Tupla con coordenadas (x, y)
coordenada = (10, 20)

# Tupla con datos de una persona
persona = ("Juan", 30, "Ingeniero")

# Accediendo a elementos por índice
print(persona[0])  # Juan

# Intentar modificar una tupla dará error
# persona[1] = 31  # Esto genera un error

# Desempaquetado de tuplas
nombre, edad, profesion = persona
print(nombre, edad, profesion)

"""
3. Conjuntos (set)
Cuándo usarlos:
Cuando necesitas almacenar elementos únicos (sin duplicados).
Para operaciones matemáticas como unión, intersección o diferencia.
Para verificar la pertenencia (in) de manera rápida.
"""

# Definiendo un conjunto de números
numeros = {1, 2, 3, 4, 5, 5, 5}  # Se eliminarán los duplicados

# Agregando un nuevo elemento
numeros.add(6)

# Eliminando un elemento
numeros.discard(3)

# Verificando si un elemento está en el conjunto
print(4 in numeros)  # True

# Operaciones con conjuntos
pares = {2, 4, 6, 8}
impares = {1, 3, 5, 7, 9}

union = pares | impares  # {1, 2, 3, 4, 5, 6, 7, 8, 9}
interseccion = pares & numeros  # Elementos comunes
print(union, interseccion)

"""
4. Diccionarios (dict)
📌 Cuándo usarlos:
Cuando necesitas almacenar datos en pares clave-valor.
Para representar objetos o datos estructurados (como JSON).
Para acceder a valores rápidamente usando una clave en lugar de un índice.
"""

# Diccionario con información de una persona
persona = {
    "nombre": "Lucía",
    "edad": 28,
    "profesion": "Doctora"
}

# Accediendo a un valor por su clave
print(persona["nombre"])  # Lucía

# Modificando un valor
persona["edad"] = 29

# Agregando una nueva clave-valor
persona["ciudad"] = "Madrid"

# Eliminando una clave-valor
del persona["profesion"]

# Recorriendo un diccionario
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

"""
5. NoneType (None)
Cuándo usarlo:
Para representar la ausencia de valor o una variable aún sin definir.
Para indicar que una función no devuelve nada.
Para restablecer una variable a un estado vacío.
"""

# Variable sin valor definido
resultado = None  

# Verificando si una variable es None
if resultado is None:
    print("No hay resultado disponible")

# Uso en funciones sin retorno
def saludo():
    print("Hola")
    
retorno = saludo()  # Esta función devuelve None
print(retorno is None)  # True

"""
Resumen: ¿Cuándo usar cada tipo de dato?
Tipo	            Cuándo usarlo
Lista (list)	    Cuando necesitas una colección ordenada y modificable.
Tupla (tuple)	    Cuando necesitas una colección fija e inmutable.
Conjunto (set)	    Cuando necesitas elementos únicos y operaciones matemáticas.
Diccionario (dict)	Cuando necesitas datos en formato clave-valor para acceso rápido.
NoneType (None)	    Cuando una variable no tiene valor o una función no devuelve nada.
"""


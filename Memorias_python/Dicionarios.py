#En Python, los diccionarios (dict) son estructuras clave-valor muy poderosas.


usuarios = {
    "Juan": 25,
    "Ana": 30,
    "Luis": 35
}

for nombre, edad in usuarios.items():
    print(f"{nombre} tiene {edad} años.")

# usuarios.items() devuelve un conjunto de tuplas (clave, valor).
# Se recorre el diccionario con un for y se imprimen los valores.


# diccionario de diccionarios

empleados = {
    "001": {"nombre": "Carlos", "edad": 28, "puesto": "Desarrollador"},
    "002": {"nombre": "María", "edad": 32, "puesto": "Gerente"},
    "003": {"nombre": "Pedro", "edad": 25, "puesto": "Diseñador"}
}

for id, datos in empleados.items():
    print(f"ID: {id}")
    for clave, valor in datos.items():
        print(f"  {clave}: {valor}")

#Se define un diccionario donde cada clave representa un ID y su valor es otro diccionario con información del empleado.
#Se usa for anidado para recorrer cada empleado y sus detalles.

#filtrar datos en un diccionario

mayores = {k: v for k, v in empleados.items() if v["edad"] > 30}
print(mayores)

#Se usa un diccionario por comprensión para filtrar empleados con edad mayor a 30.


# contar palabras en un texto con diccionarios

texto = "python es genial y python es fácil de aprender"
palabras = texto.split()

contador = {}

for palabra in palabras:
    contador[palabra] = contador.get(palabra, 0) + 1

print(contador)

# invertir un diccionario

paises = {"Colombia": "Bogotá", "Francia": "París", "Japón": "Tokio"}

invertido = {v: k for k, v in paises.items()}
print(invertido)

#Uso de defaultdict para agrupar datos

from collections import defaultdict

nombres = ["Ana", "Andrés", "Carlos", "Carmen", "David"]
grupo = defaultdict(list)

for nombre in nombres:
    grupo[nombre[0]].append(nombre)

print(dict(grupo))

# unión de diccionarios

productos_a = {"Laptop": 1000, "Mouse": 50}
productos_b = {"Teclado": 80, "Monitor": 300}

productos_a.update(productos_b)
print(productos_a)

#Diccionario con funciones como valores

def suma(a, b): return a + b
def resta(a, b): return a - b

operaciones = {"sumar": suma, "restar": resta}

print(operaciones["sumar"](5, 3))  # Llama a la función suma
print(operaciones["restar"](10, 4))  # Llama a la función resta

#Ordenar un diccionario por valores

productos = {"Laptop": 1000, "Mouse": 50, "Teclado": 80, "Monitor": 300}
ordenado = dict(sorted(productos.items(), key=lambda x: x[1]))

print(ordenado)

#buscar el valor maximo

productos = {"Laptop": 1000, "Mouse": 50, "Teclado": 80, "Monitor": 300}
producto_mas_caro = max(productos, key=productos.get)

print(producto_mas_caro)


#Crear un diccionario	{} o dict()
persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Madrid"
}

persona_nueva = dict(nombre="Carlos", edad=30, ciudad="Barcelona")
print(persona_nueva)
print(persona)

#Acceder a un valor	dic["clave"]
print(persona["nombre"])
#Modificar un valor	dic["clave"] = valor
persona["edad"] = 26
print(persona)
#Agregar un elemento	dic["nueva_clave"] = valor
persona["profesion"] = "Ingeniera"
print(persona)
#Eliminar un elemento	del dic["clave"] / pop()
del persona["ciudad"]
print(persona)
#eliminar un elemento con pop
edad = persona.pop("edad")
print(f"Edad eliminada: {edad}")
print(persona)
#Obtener un valor sin error	get()
print(persona.get("ciudad", "No disponible"))
#Obtener claves	keys()
print(persona.keys())
#Obtener valores	values()
print(persona.values())
#Obtener pares clave-valor	items()
print(persona.items())
#Recorrer con for	for clave, valor in dic.items()
for clave, valor in persona.items():
    print(f"{clave}: {valor}")
#Verificar existencia de clave	"clave" in dic
if "nombre" in persona:
    print("La clave 'nombre' está en el diccionario")
#Copiar un diccionario	copy()
persona_copia = persona.copy()
print(persona_copia)
#Fusionar diccionarios	update()
extra = {"pais": "España", "edad": 27}
persona.update(extra)
print(persona)
#Usar setdefault() para agregar una clave solo si no existe
persona.setdefault("telefono", "No disponible")
print(persona)
# eliminar todos los elementos con clear
persona.clear()
print(persona)
#Crear con comprensión	{x: f(x) for x in iterable}
numeros = {x: x**2 for x in range(1, 6)}
print(numeros)
#Convertir listas a diccionario	dict(zip(claves, valores))
claves = ["nombre", "edad", "ciudad"]
valores = ["Pedro", 29, "Sevilla"]

diccionario = dict(zip(claves, valores))
print(diccionario)
#Contar elementos de una lista	Counter(lista)
from collections import Counter

lista = ["rojo", "azul", "rojo", "verde", "azul", "azul"]
conteo = dict(Counter(lista))

print(conteo)

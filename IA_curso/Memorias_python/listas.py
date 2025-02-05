#Recorrer una lista con enumerate()

frutas = ["Manzana", "Banana", "Cereza"]

for indice, fruta in enumerate(frutas):
    print(f"Índice {indice}: {fruta}")

#Filtrar elementos con list comprehension

numeros = [10, 15, 20, 25, 30, 35, 40]
pares = [num for num in numeros if num % 2 == 0]

print(pares)

#Encontrar el valor máximo y su índice

numeros = [8, 3, 15, 7, 9]
maximo = max(numeros)
indice = numeros.index(maximo)

print(f"El número más grande es {maximo} en la posición {indice}")

#ordenar una lista de diccionarios por clave

empleados = [
    {"nombre": "Carlos", "edad": 28},
    {"nombre": "Ana", "edad": 22},
    {"nombre": "Luis", "edad": 35}
]

ordenado = sorted(empleados, key=lambda x: x["edad"])

print(ordenado)

#Aplanar una lista de listas (flatten)

listas = [[1, 2, 3], [4, 5], [6, 7, 8]]
aplanada = [num for sublista in listas for num in sublista]

print(aplanada)

#eliminar los duplciados manteniendo el orden

numeros = [1, 2, 2, 3, 4, 4, 5]
unicos = list(dict.fromkeys(numeros))

print(unicos)

#rotar una lista

def rotar_lista(lista, n):
    n = n % len(lista)  # Evita rotaciones mayores al tamaño de la lista
    return lista[-n:] + lista[:-n]

numeros = [1, 2, 3, 4, 5]
rotada = rotar_lista(numeros, 2)

print(rotada)

# intercalar una dos listas en una sola

a = [1, 3, 5]
b = [2, 4, 6]
intercalada = [num for pareja in zip(a, b) for num in pareja]

print(intercalada)

#generar una lsia de numeros primos

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

primos = [num for num in range(2, 50) if es_primo(num)]

print(primos)

#Combinar multiples listas con zip_longest

from itertools import zip_longest

a = ["A", "B", "C"]
b = [1, 2]
c = ["X", "Y", "Z"]

combinada = list(zip_longest(a, b, c, fillvalue="-"))

print(combinada)

 # enumerate() para índices.
 # list comprehension para filtrar y transformar.
 # sorted() con key para ordenar listas de diccionarios.
 # zip() y zip_longest() para combinar listas.
 # Algoritmos avanzados como rotación, eliminación de duplicados y búsqueda de primos.


#Acción	Método / Operador
#Crear lista	[]
frutas = ["Manzana", "Banana", "Cereza"]
print(frutas)
#Acceder a un elemento	lista[i]
print(frutas[0])  # Primer elemento
print(frutas[-1])  # Último elemento
#Modificar un elemento	lista[i] = valor
frutas[1] = "Pera"
print(frutas)
#Agregar elemento al final	append()
frutas.append("Uva")
print(frutas)
#Insertar en una posición espesifica	insert()
frutas.insert(1, "Mango")  # Inserta "Mango" en la posición 1
print(frutas)
#Eliminar por valor	remove()
frutas.remove("Mango")
print(frutas)
#Eliminar por índice	pop()
frutas.pop(2)  # Elimina el elemento en la posición 2
print(frutas)
#Vaciar la lista	clear()
frutas.clear()
print(frutas)
#Contar ocurrencias	count()
numeros = [1, 2, 2, 3, 4, 2, 5]
print(numeros.count(2))  # Cuenta cuántas veces aparece el 2
#Encontrar índice	index()
print(numeros.index(3))  # Encuentra la posición del número 3
#Ordenar	sort()
numeros.sort()
print(numeros)
#Invertir orden	reverse()
numeros.sort(reverse=True)
print(numeros)

numeros.reverse()
print(numeros)

#Copiar lista	copy()
copia_numeros = numeros.copy()
print(copia_numeros)
#Extender lista	extend()
nueva_lista = [6, 7, 8]
numeros.extend(nueva_lista)
print(numeros)

#Concatenar listas	+
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
concatenada = lista1 + lista2
print(concatenada)

#Crear lista con rango	range()
numeros = list(range(1, 11))
print(numeros)

#Mapear valores	map()
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados)

#Filtrar valores	filter()
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)

#Combinar listas	zip()
nombres = ["Ana", "Luis", "Pedro"]
edades = [25, 30, 35]

combinado = list(zip(nombres, edades))
print(combinado)

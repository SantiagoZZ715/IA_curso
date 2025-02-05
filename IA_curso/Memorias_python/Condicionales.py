"""
Los condicionales en Python son estructuras de control que permiten ejecutar bloques de código diferentes dependiendo 
de si se cumple o no una condición. 
En otras palabras, permiten que el programa tome decisiones basadas en el valor de las expresiones lógicas,
 comparaciones o evaluaciones que se realicen.
"""

"""
if - Condicional simple
Ejecuta un bloque de código si una condición es verdadera.
"""
edad = 18

if edad >= 18:
    print("Eres mayor de edad.")
"""
if-else - Condicional con alternativa
Ejecuta un bloque si la condición es verdadera, y otro si es falsa.
"""
edad = 16

if edad >= 18:
    print("Puedes votar.")
else:
    print("No puedes votar.")

"""
if-elif-else - Múltiples condiciones
Permite evaluar varias condiciones en secuencia.
"""

temperatura = 25

if temperatura < 15:
    print("Hace frío.")
elif 15 <= temperatura < 25:
    print("El clima es templado.")
else:
    print("Hace calor.")

"""
if con operadores lógicos (and, or, not)
Permite combinar condiciones.
"""
hora = 14
es_dia_libre = True

if hora >= 9 and hora <= 18 and not es_dia_libre:
    print("Estoy trabajando.")
else:
    print("Estoy libre.")

"""
 if con in (Verificar pertenencia)
 Comprueba si un valor está dentro de una lista, tupla o cadena.
"""
frutas = ["manzana", "pera", "uva"]

if "pera" in frutas:
    print("Sí, hay peras.")
else:
    print("No hay peras.")

"""
if con is (Comparación de identidad)
Comprueba si dos variables apuntan al mismo objeto en memoria.
"""

x = None

if x is None:
    print("La variable es None.")
else:
    print("La variable tiene un valor.")

"""
if con match-case (Alternativa a if-elif-else, Python 3.10+)
"""

color = "rojo"

match color:
    case "rojo":
        print("El color es rojo.")
    case "azul":
        print("El color es azul.")
    case _:
        print("Color no reconocido.")

"""
if en una sola línea (Operador ternario)
"""
edad = 20
mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"
print(mensaje)

"""
if anidado (Condicionales dentro de condicionales)
Evalúa una condición dentro de otra.
"""

edad = 25
tiene_identificacion = True

if edad >= 18:
    if tiene_identificacion:
        print("Puedes entrar.")
    else:
        print("Necesitas identificación.")
else:
    print("No puedes entrar.")

"""
if con all() y any() (Evaluar múltiples condiciones a la vez)

all() verifica si todas las condiciones son True.
any() verifica si al menos una es True.
"""

numeros = [4, 8, 10, 12]

if all(n % 2 == 0 for n in numeros):
    print("Todos los números son pares.")
else:
    print("Al menos uno es impar.")

if any(n > 10 for n in numeros):
    print("Al menos un número es mayor que 10.")

"""
 Resumen de condicionales en Python
Condicional	Uso
if	                        Evalúa una sola condición.
if-else	                    Ejecuta un bloque si es True, otro si es False.
if-elif-else        	    Evalúa múltiples condiciones en secuencia.
if con and, or, not     	Combina condiciones.
if con in	                Verifica si un elemento está en una lista, tupla o cadena.
if con is	                Verifica si dos variables apuntan al mismo objeto.
match-case	                Alternativa estructurada a if-elif-else (Python 3.10+).
if en una línea (ternario)	Forma compacta de if-else.
if anidado	                if dentro de otro if.
if con all() y any()	    Evalúa listas de condiciones.
"""



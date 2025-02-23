

"""
usuario = input("Escriba su nombre: ")
productos = ['pera','banano','manzana','guayaba']
n_productos = int(input("cuantos productos desea comprar "))
valortotal = 0


for i in range(n_productos):
    valortotal = int(input("precio pera:5000 , banano: 6000, manzana: 8000, guayaba: 2000 "))   
    valortotal += valortotal   

print("el valor total de su compra es: ")
print(valortotal)
cambio = int(input("con cuanto desea pagar "))
valorfinal = cambio - valortotal
print("muchas gracias por su compra: " + usuario + " su cambio es: ")
print(valorfinal)
 

"""


"""
solicitar al usuario cuantos numeros quiere guardar y sacar de esa lista
promedio 
maximo
minimo
sumatoria

"""
# Solicitar al usuario cuantos numeros quiere guardar
cantidad = int(input("¿Cuántos números quieres guardar? "))

# Inicializar la lista para guardar los números
numeros = []

# Solicitar los números al usuario
for i in range(cantidad):
    numero = float(input("Introduce un número: "))
    if numero < 12:
        numero = float(input("el numero ingresado es muy bajo ingrese uno nuevamente: "))
        numeros.append(numero)
    else:
        numeros.append(numero)


# Calcular el promedio
promedio = sum(numeros) / cantidad

# Calcular el máximo
maximo = max(numeros)

# Calcular el mínimo
minimo = min(numeros)

# Calcular la sumatoria
sumatoria = sum(numeros)

# Imprimir los resultados
print(f"Promedio: {promedio}")
print(f"Máximo: {maximo}")
print(f"Mínimo: {minimo}")
print(f"Sumatoria: {sumatoria}")







  




"""
edad = int(input("ingrese su edad")) 

if  edad < 6:
    print ("Primera infancia")
elif edad > 6 and edad < 13:
    print ("Niñez")
elif edad > 13 and edad <= 17:
    print ("Adolecencia")
elif edad > 18:
    print ("mayor de edad")
"""



"""
crear un diccionario con personas mayores de edad 
"""


"""
edad = int(input("ingrese su edad: "))
if edad >= 18:
    nombre = input("ingrese su nombre")
    apellido = input("ingrese su apellido")
    mayor_edad = {
        "nombres": nombre,
        "apellidos": apellido,
        "edades": edad
    }
    print(mayor_edad["nombres"] +" " + mayor_edad["apellidos"] + " " + str(mayor_edad["edades"]))


# Solicitar al usuario cuántas personas quiere registrar
cantidad_personas = int(input("¿Cuántas personas quieres registrar? "))

# Inicializar el diccionario para guardar las personas mayores de 18 años
personas_mayores = {}

# Solicitar los nombres, apellidos y edades de las personas
for i in range(cantidad_personas):
    edad = int(input("Introduce la edad de la persona: "))
    if edad > 18:
        nombre = input("Introduce el nombre de la persona: ")
        apellido = input("Introduce el apellido de la persona: ")
        personas_mayores[nombre] = {
            "apellido": apellido,
            "edad": edad
        }

# Imprimir el diccionario de personas mayores de 18 años
print("Personas mayores de 18 años:")
for nombre, datos in personas_mayores.items():
    print(f"{nombre} {datos['apellido']} {datos['edad']}")
"""






 





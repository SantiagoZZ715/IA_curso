"""
Un módulo en Python es un archivo que contiene definiciones y declaraciones de Python,
como funciones, clases, variables y código ejecutable. Los módulos permiten organizar
y reutilizar el código en diferentes partes de un programa o incluso en proyectos diferentes.

Los módulos son una forma de abstraer funcionalidades y permiten estructurar el código de manera más modular,
manteniendo el proyecto limpio y fácil de mantener.

¿Cómo usar un módulo?
Para usar un módulo en Python, se utiliza la palabra clave import, seguida del nombre del módulo.

"""

"""
El módulo math se importa y luego se utiliza su función sqrt para calcular la raíz cuadrada de 16.
"""

import math

# Usamos la función sqrt() del módulo math
resultado = math.sqrt(16)
print(resultado)  # Imprime: 4.0

"""
Ejemplo de importación y uso de un módulo de terceros:

pip install requests ( pip es el administrador de paquetes de Python.)

"""


import requests

response = requests.get("https://api.github.com")
print(response.status_code)



import mi_modulo

print(mi_modulo.saludar("Juan"))  # Imprime: Hola, Juan!
print(mi_modulo.mi_variable)      # Imprime: Soy una variable del módulo

"""
Formas de importar elementos de un módulo:
"""

"""
Importar todo el módulo
"""

import math
resultado = math.pow(2, 3)  # Usamos la función pow del módulo math
print(resultado)  # Imprime: 8.0

"""
Importar funciones específicas de un módulo:
"""

from math import sqrt
resultado = sqrt(25)  # Usamos solo la función sqrt
print(resultado)  # Imprime: 5.0

"""
Importar un módulo con un alias:
"""

import math as m
resultado = m.factorial(5)  # Usamos la función factorial con el alias m
print(resultado)  # Imprime: 120

"""
Ventajas de usar módulos:
Organización: Los módulos ayudan a organizar el código en bloques lógicos.
Reutilización: Puedes reutilizar el código de un módulo en diferentes programas sin tener que copiarlo.
Legibilidad: Facilitan la lectura del código al separar funcionalidades específicas.
Mantenimiento: Al tener código modular, es más fácil realizar cambios o mejoras sin afectar todo el programa.
"""


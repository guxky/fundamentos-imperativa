"""
Dada la lista temperaturas_celsius = [0, 20, 37, 100],
crea una list comprehension que convierta cada valor a Fahrenheit.
"""
temperaturas_celsius = [0, 20, 37, 100]
temperaturas_fahrenheit = [c*9/5 + 32 for c in temperaturas_celsius]

print(temperaturas_fahrenheit)

"""
Dada la lista palabras = ["sol", "luna", "mar", "estrella", "rio", "montaña"], 
crea una list comprehension que se quede solo con las palabras de más de 3 letras.
"""

palabras = ["sol", "luna", "mar", "estrella", "rio", "montaña"]
palabras_filtro = [p for p in palabras if len(p) > 3]

print(palabras_filtro)

""""
Crear una list comprehension dada la lista numeros = [1, 2, 3, 4, 5] 
para saber en que posicion son pares e impares
"""

numeros = [1, 2, 3, 4, 5]
numeros_filtro = ["par" if n % 2 == 0 else "impar" for n in numeros]

print(numeros_filtro)


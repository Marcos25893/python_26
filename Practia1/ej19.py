#19. Lista de palabras únicas

#Pide al usuario que introduzca una frase y construye una lista con las palabras que aparecen sin repeticiones,
#  manteniendo el orden en el que aparecen.

frase = input("Dime una frase: ")

palabras = list()

palabras = frase.split(" ")

resultado = []
repetidos = set()

for palabra in palabras:
    if palabra not in repetidos:
        resultado.append(palabra)
        repetidos.add(palabra)

print(resultado)


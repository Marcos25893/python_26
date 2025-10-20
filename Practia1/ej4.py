palabra = input("Dime una palabra: ")
vocales = "aeiouAEIOU"

contador=0
for letra in palabra:
    if letra in vocales:
        contador += 1

print("La palabra",  palabra,  "tiene", contador, "vocales.")
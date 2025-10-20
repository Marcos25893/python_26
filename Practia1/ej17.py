# 17. Producto escalar de dos listas

#Solicita dos listas de números de igual longitud y calcula el producto escalar (sumando el producto de los elementos en la misma posición).

lista1 = []
for i in range(5):
    numero = input("Dime un numero para la lista1: ")
    lista1.append(numero)

lista2 = []
for i in range(5):
    numero = input("Dime un numero para la lista2: ")
    lista2.append(numero)

resultado = 0
for i in range(len(lista1)):
    resultado += int(lista1[i]) * int(lista2[i])

print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("El producto escalar es:", resultado)

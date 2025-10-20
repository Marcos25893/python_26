matriz = list()
for i in range(0,2):
    
    matriz.append(list(range(3)))
    for j in range(0,3):
        numero = int(input("Dime un número"))
        print(i,j)
        matriz[i][j] = numero
        
print(matriz)

contador = 0
for fila in matriz:
    contador += sum(fila)
print(contador)

mtx = [list(range(3)) for _ in range(2)]
print(mtx)
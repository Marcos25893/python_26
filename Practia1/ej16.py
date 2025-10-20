# 16. Lista ordenada

#Pide al usuario ingresar varios números, guárdalos en una lista y muestra:

#- La lista original.  
#- La lista ordenada ascendentemente.  
#- La lista ordenada descendentemente.  

numeros = []
for i in range(5):
    numero = input("Dime un numero: ")
    numeros.append(numero)

print(numeros) # lista original
print(sorted(numeros)) # lista ordenada ascendentemente
print(sorted(numeros, reverse=True)) # lista ordenada descendentemente
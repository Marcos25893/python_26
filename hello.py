#Este es mi primer programa en Python
print("Hola Mundo")

print("Otra cosa")

print(type(3.25)) #Nos dice el tipo de dato

numero = 100
cadena = "Hola Mundo"
flotante = 3.25
booleano = True

print(numero)
print(cadena)
print(flotante)
print(booleano)

print(type(numero))
print(type(cadena))
print(type(flotante))
print(type(booleano))

#El tipo de dato de una variable puede cambiar
numero = "Ahora soy una cadena"
print(numero)

numero = 50
print(numero)

#Si es del mismotipo de dato queda bien, sin son diferentes mejor no
numero1, numero2, numero3 = 10, 20, 30
cadena1, cadena2, cadena3 = "Hola", "Mundo", "Python"

print( reversed("Hola Mundo"))

area = 3.14 * pow(5, 2)
print("El area es:", area)#Con la coma añade un espacio
print("El area es: " + str(area))#Con el + no añade espacio, pero hay que convertir a cadena no se puede mezclar tipos de datos

print(isinstance(area, float)) #Nos dice si es del tipo de dato que le indicamos

print(len(cadena1)) #Nos dice la longitud de la cadena

edad = input("Dime tu edad: ") #Input siempre devuelve una cadena
print("Tu edad es: " + edad)
print(type(edad))

edad = int(edad) #Convertimos la cadena a entero
print(type(edad))

precio = float(input("Dime el precio: ")) #Convertimos directamente a float
print("El precio es: " + str(precio))
edad = int(input("Dime que edad tienes: "))

if edad >= 65:
    print( "Eres mayor")
elif (edad >= 18) and (edad < 65):
    print( "Eres adulto")
else:
    print( "Eres menor de 18")

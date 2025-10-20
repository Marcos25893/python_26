# 20. Inventario con diccionario

#Crea un programa que simule un pequeño inventario de productos mediante un diccionario:  

#- Cada clave es el nombre de un producto, y el valor, la cantidad disponible.  
#- Permite al usuario añadir productos, modificar cantidades y mostrar el inventario final.

inventario = {}
opcion=0

while opcion!=4:
    print("1. Añadir producto")
    print("2. Modificar cantidad")
    print("3. Mostrar inventario")
    print("4. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre del producto: ")
        cantidad = int(input("Cantidad: "))
        inventario[nombre] = cantidad

    elif opcion == "2":
        nombre = input("Producto a modificar: ")
        if nombre in inventario:
            cantidad = int(input("Nueva cantidad: "))
            inventario[nombre] = cantidad
        else:
            print("Ese producto no existe.")

    elif opcion == "3":
        print("\nInventario:")
        for producto, cantidad in inventario.items():
            print(producto, "->", cantidad)

    elif opcion == "4":
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida.")

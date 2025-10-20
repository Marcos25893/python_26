#18. Combinación de diccionarios

#Crea dos diccionarios con claves y valores numéricos, y combina ambos en uno solo:

#- Si una clave se repite, suma los valores.  
#- Si no, simplemente añade la clave y su valor. 

diccionario1 = {
    "primero": 5,
    "segundo": 8,
    "tercero": 23
}

diccionario2 = {
    "cuarto": 14,
    "quinto": 2,
    "primero": 7
}

#dict_combined = diccionario1.copy()  # Copia dict1 para empezar
for clave, valor in diccionario1.items():
    if clave in diccionario2:
        diccionario2[clave]=diccionario1[clave] + diccionario2[clave]
    else:
        diccionario2[clave] = diccionario1[clave]
        
print(diccionario2)



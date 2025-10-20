num = int(input("Dime un número entero: "))
factorial = 1
for i in range(1, num+1):
    factorial *= i
    
print("El factorial de", num, "es", factorial)
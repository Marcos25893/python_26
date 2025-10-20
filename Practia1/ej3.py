num1 = int(input("Dime un número entero: "))
num2 = int(input("Dime otro número entero: "))

if num1 > num2:
    num1, num2 = num2, num1

for i in range(num1, num2+1):
    if i % 2 == 0:
        print(i)

par = [i for i in range(num1, num2+1) if i%2 == 0]
print(par)

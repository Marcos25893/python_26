from os import getcwd, mkdir
from statistics import mean
from math import * #Nos ahorra escribir math. cada vez que queramos usar una función de math

print("Current Working Directory:", getcwd())
print("Create folder trash:", "mkdir trash")
#mkdir('trash')    # Create a directory named 'trash' in the current working directory

data = [10, 20, 30, 40, 50]
print("Mean of data:", mean(data))

print("Square root of 16:", sqrt(16))
print(pi)
print(pow(2, 5))
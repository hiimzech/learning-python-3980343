# LinkedIn Learning Python course by Joe Marini
# Working with modules of code

# import the math module, which contains features for working with mathematics
import math

num = 2
print(f"the square root of {num} is {math.sqrt(num)}.")

# import a specific part of the module so you can refer to it more easily
from math import pi as g

print("Pi is",g)

# import a module and give it a different name
import random as r

# the math module contains lots of pre-built functions


# in addition to functions, some modules contain useful constants 


# Generate a random number between 100 and 200
print("A random number",r.randint(100,200))
print("A random number",r.randint(100,200))
print("A random number",r.randint(100,200))

# try some of the math functions for yourself here:

# Use the 3rd party tabulate module to print tabulated data:
#https://pypi.org/project/tabulate/
#pip install tabulate

from tabulate import tabulate

# Sample data
data = [
  ["Product", "Price", "Stock"],
  ["Laptop", 999.99, 45],
  ["Mouse", 24.99, 128],
  ["Keyboard", 59.99, 89]
]

# Create a formatted table
print(tabulate(data,headers="firstrow",tablefmt="fancy_grid"))
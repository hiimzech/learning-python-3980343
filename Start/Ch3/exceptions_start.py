# LinkedIn Learning Python course by Joe Marini
# Example file for working with Exceptions
#

# Errors can happen in programs, and we need a clean way to handle them
# This code will cause an error because you can't divide by zero:

# Exceptions provide a way of catching errors and then handling them in 
# a separate section of the code to group them together

#x = 1/0
try:
  x = 1/0
except:
  print("broken")

# You can also catch specific exceptions

try:
  answer = input("what should I divide 1 by?")
  num = int(answer)
  print(1/num)
except ZeroDivisionError as z:
  print("error:",z)
except ValueError as v:
  print("error:",v)
finally:
  print("finally always triggers")
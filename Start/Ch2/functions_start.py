# LinkedIn Learning Python course by Joe Marini
# Example file for working with functions


# define a basic function
def printing_func():
  print("hello world!")
  name = input("What is your name? ")
  print("Nice to meet you,", name)

printing_func()  

# function that takes parameters
def printing_func(myname):
  print("hello "+ myname)
  name = input("What is your name? ")
  print("Nice to meet you,", name)

printing_func("avava")    

# function that returns a value
def cube(x):
  return x*x*x

result = cube(3)
print(result)
print(cube(2))

# function with default value for an parameter
def printing_func(myname,greetings=None):
  if greetings == None:
    greet = input("what greetings? ")
    print(greet+" "+ myname)
  else:
    print("hello "+ myname)
  name = input("What is your name? ")
  print("Nice to meet you,", name)

printing_func("avava",)    

# function with variable number of parameters
def multi_param(*args):
  result = 0
  for x in args:
    result = result + x
  return result

def multi_param(start,*args):
  result = start
  for x in args:
    result = result + x
  return result

print(multi_param(1,2,4,5,3))
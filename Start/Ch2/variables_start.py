# LinkedIn Learning Python course by Joe Marini
# Example file for variables and basic types


# Basic data types in Python: Numbers, Strings, Booleans 
# Variable names must start with a letter or _, and can have numbers. They are case sensitive. 
myint = 10
myfloat = 13.2576
mystr = "This is a string"
mybool = True

# We can display the content of a variable using the print() function
print(myint,myfloat,mystr,mybool)

# Operators are used to perform operations on variables
print(myint + myfloat)
print(myint * myfloat)
print(myint - myfloat)
print(myint / myfloat)
print(myint % 3)

mystr2 = "asdf"
print(mystr + mystr2)
print("10" * 3)
# print("mystr" + 1)

# Logical and comparison operators 
print(myint == 10)
print(myint != 30)
print(myint > 20)
print(myint < 10)
print(myint >= 20)
print(myint <= 10)

print(myint > 5 and myfloat < 22.1)
print(myint > 5 or myfloat < 22.1)
print(not(myint > 5 or myfloat < 22.1))

# re-declaring a variable works
myint = "sss"
print(myint)

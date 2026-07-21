# LinkedIn Learning Python course by Joe Marini
# Example file for complex types

# Sequences: Lists and Tuples
# These are -- surprise -- sequences of values
mylist = [0,1,"two",3.14,False]
print(len(mylist))

# to access a member of a sequence type, use []
print(mylist[3])
print(mylist[-1])
mylist2 = mylist
mylist2[1] = 100
print(mylist2[1])

# add a list to another list
mylist3 = mylist + mylist2
print(mylist3)

mystr = "this is a string"
print(mystr[2])
# mystr[2] = "a"

# use slices to get parts of a sequence
print(mylist[1:4:2])
print(mylist[::2])

# you can use slices to reverse a sequence
print(mylist[::-1])

# Tuples are like lists, but they are immutable
mytuple = (0,"one",2,True)
print(mytuple[1])

# Sets are also sequences, but they contain unique values
myset = {0,1,2,2,"three",}
print(myset)

# Set, however, can not be indexed like lists or tuples
# print(myset[0]) # this will cause an error

# Test for membership
print(3.14 in mylist)
print(2 in mytuple)
print("three" in myset)
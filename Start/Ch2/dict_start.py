# LinkedIn Learning Python course by Joe Marini
# Example file for complex types

# Dictionary: a key-value data structure
mydict = {
  1:"asdf",
  2: "ffff",
  "three":3,
  4.5:["four","five","six"]
  }

print(mydict)

# dictionaries are accessed via keys
print(mydict["three"])

# you can also set dictionary data by creating a new key
mydict["seven"] = "333"

print(mydict)

# Trying to access a nonexistent key will produce an error
#print(mydict["qqqq"])

# To avoid this, you can use the "in" operator to see if a key exists
print("three" in mydict)
print("qqqq" in mydict)

# You can retrieve all of the keys and values from a dictionary
print(mydict.keys())
print(mydict.values())

# You can also iterate over all the items in a dictionary
for key, val in mydict.items():
  print(key,val)
# LinkedIn Learning Python course by Joe Marini
# Example file for working with loops


x = 0

# define a while loop
while x < 5:
  print(x)
  x = x + 1

answer = input("do i stop?")
while answer!= "yes":
  print(answer)

# define a for loop
days = ["mon","tues","wed","thurs","fri"]
for i in days:
  print(i)

# use a for loop over a collection


# use the break and continue statements
for i in days:
  if (i == "wed"):
    print("skip")
    break
  print(i)

for i in days:
  if (i == "thurs"):
    print("continue")
    continue
  print(i)  

# using the enumerate() function to get an index and an item
for index,elem in enumerate(days):
  print(index,elem)
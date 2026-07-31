# Python code​​​​​​‌‌‌‌‌‌‌‌​‌‌‌​‌‌​​​‌​‌‌‌​‌ below
# Use print("messages...") to debug your solution.

show_expected_result = False
show_hints = False

def find_largest(numbers):
    # Your code goes here
  count = 0
  for str in numbers:
    if count < len(str):
      count = len(str)     

  return count

# This is how your code will be called.
# Your answer should be the length of the longest string in the list
# You can edit this code to try different testing cases.
test_strings = [
    "Hello World!",
    "And how can this be? For he is the Kwisatz Haderach!",
    "Four score and seven years ago",
    "Life moves pretty fast. If you don't stop and look around once in a while, you could miss it."
]

print(find_largest(test_strings))
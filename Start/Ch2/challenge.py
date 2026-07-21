# Python code​​​​​​‌‌‌‌‌‌‌​‌​‌‌‌‌‌​‌​​‌​‌​‌‌ below
# Use print("messages...") to debug your solution.

show_expected_result = False
show_hints = False

def count_numbers(which, numbers):
    # Your code goes here
    odd = 0
    even = 0
    
    for i in numbers:
        if i % 2 == 0:
            even = even + 1
        elif i%2 != 0:
            odd = odd + 1

    if which == "even":
        return even
    elif which == "odd":
        return odd    
    return -1

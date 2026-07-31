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
        if (even == 1):
            return print("there is", even, "even number in", numbers)

        return print("there are", even, "even numbers in", numbers)
    elif which == "odd":
        if (odd == 1):
            return print("there is", odd, "odd number in", numbers)
        
        return print("there are", odd, "odd numbers in", numbers)
    
    return -1

numlist = [7, 17, 2, 13, 19, 20, 0, 5, 11, 1280, 105]
count_numbers("even",numlist)
count_numbers("odd",numlist)
count_numbers("Blarg",numlist)
# Python code​​​​​​‌‌‌‌‌‌‌‌​‌‌‌‌​‌‌​​​​​​​‌​ below
# Use print("messages...") to debug your solution.

show_expected_result = False
show_hints = False

import calendar as c

def count_days(year, month, whichday):
    # Your code goes here.
    cal = c.monthcalendar(year,month)

    count = 0
    for i in cal:
        #print(i[whichday])
        if i[whichday] > 0:
            count = count + 1

    return count


# This is how your code will be called.
# You can edit this code to try different testing cases.
testyear = 2025
testmonth = 12
testday = 0

print(count_days(testyear, testmonth, testday))

testyear = 2030
testmonth = 1
testday = 5

print(count_days(testyear, testmonth, testday))

testyear = 2027
testmonth = 7
testday = 5

print(count_days(testyear, testmonth, testday))
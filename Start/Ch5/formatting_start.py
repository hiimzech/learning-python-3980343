
#
# Example file for formatting time and date output
# LinkedIn Learning Python course by Joe Marini
#


from datetime import datetime

# Times and dates can be formatted using a set of predefined string
# control codes 
now = datetime.now()

#### Date Formatting ####

# %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
print("the current year is :",now.strftime("%y"))
print("the current weekday is :",now.strftime("%a"))
print("the current month is :",now.strftime("%b"))
print("the current day of month is :",now.strftime("%d"))
print("the current date is ",now.strftime("%d"),now.strftime("%b"),now.strftime("%y"))
print(now.strftime("the current date is %d/%b/%y"))

# %c - locale's date and time, %x - locale's date, %X - locale's time
print(now.strftime("Locale date and time: %c"))
print(now.strftime("Locale date: %x"))
print(now.strftime("Locale time: %X"))

#### Time Formatting ####

# %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
print(now.strftime("the current time is %H:%M:%S %p"))
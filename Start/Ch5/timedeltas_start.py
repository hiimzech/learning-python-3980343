#
# Example file for working with timedelta objects
# LinkedIn Learning Python course by Joe Marini
#


from datetime import date
from datetime import datetime
from datetime import timedelta #timespan

# construct a basic timedelta and print it
print(timedelta(days=365,hours=5,minutes=1))

# print today's date
now = datetime.now()
print(now.strftime("the current date is %d/%b/%y"))

# print today's date one year from now
print("in one year it will be", now + timedelta(days=365))

# create a timedelta that uses more than one argument
print("in two weeks and three days it will be", now + timedelta(weeks=2,days=3))

# calculate the date 1 week ago, formatted as a string
t = datetime.now() - timedelta(weeks=1)
#s = t.strftime("%d-%b-%y")
s = t.strftime("%A %B %d %y")
print("one week ago it was",s)

### How many days until April Fools' Day?
today = date.today()
afd = date(today.year,4,1)

if afd < today:
  print(f"April Fools' Day already went by {(today-afd).days} days ago")
  afd = afd.replace(year=today.year+1)

nafd = afd - today
print(f"its {nafd.days} days to the next April Fools' Day")
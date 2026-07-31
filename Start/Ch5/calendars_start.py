#
# Example file for working with Calendars
# LinkedIn Learning Python course by Joe Marini
#


import calendar

# create a plain text calendar
c = calendar.TextCalendar(calendar.SUNDAY)
str = c.formatmonth(2026,1,0,0)
print(str)

# create an HTML formatted calendar
h = calendar.HTMLCalendar(calendar.SUNDAY)
str2 = h.formatmonth(2026,2,True)
print(str2)

# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
for i in c.itermonthdays(2026,8):
  print(i)
  
# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
for m in calendar.month_name:
  print(m)

for d in calendar.day_abbr:
  print(d)

# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
print("team meetings in 2026 will be on:")

for a in range(1,13,1): #get each month of a year
  cal = calendar.monthcalendar(2026,a)
  weekone = cal[0] #first friday might be in week 1 of month a
  weektwo = cal[1] #first friday might be in week 2 of month a
  if weekone[calendar.FRIDAY] != 0: #if there's a friday here
    meetday = weekone[calendar.FRIDAY]
  else: #friday must be here
    meetday = weektwo[calendar.FRIDAY]
  print(f"{calendar.month_name[a]}: {meetday}")
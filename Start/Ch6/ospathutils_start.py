#
# Example file for working with os.path module
# LinkedIn Learning Python course by Joe Marini
#
import os
from os import path

# Print the name of the OS
print(os.name)

# Check for item existence and type
print("item exists:",path.exists("./Start/Ch6/textfile.txt"))
print("item is a file:", path.isfile("./Start/Ch6/textfile.txt"))
print("item is a directory:", path.isdir("./Start/Ch6/textfile.txt"))

# Work with file paths
print("item path:",path.realpath("./Start/Ch6/textfile.txt"))
print("item path and name:", path.split(path.realpath("./Start/Ch6/textfile.txt")))
      

# Get the modification time
import time
from datetime import date

t = time.ctime(path.getmtime("./Start/Ch6/textfile.txt"))
print(t)
print(date.fromtimestamp(path.getmtime("./Start/Ch6/textfile.txt")))

# Calculate how long ago the item was modified
td = date.today() - date.fromtimestamp(path.getmtime("./Start/Ch6/textfile.txt"))
print(f"it has been {td.days} days since we updated the file")
if td.days == 0:
  print(f"it has been {td.total_seconds()} seconds since we updated the file today")


# Python code​​​​​​‌‌‌‌‌‌‌‌‌​​‌‌‌‌​​‌‌​​‌​​‌ below
# Use print("messages...") to debug your solution.

show_expected_result = False
show_hints = False

import os
from os import path

def file_info():
    # Your code goes here.
  #dir = "./Start/Ch6/deps/"
  dir = "deps/"
  if path.isdir(dir):    
    files = os.listdir(dir)
    print(files)

    size = 0
    for file in files:
      checkfile = dir+file
      if path.isfile(checkfile) and checkfile.endswith(".txt"):
        #print(path.realpath(checkfile))
        size = size + os.path.getsize(path.realpath(checkfile))

    return size
  return 0


# This is how your code will be called.
# Your answer should be the total number of bytes of all text files in the "deps" folder.
print(file_info())
#
# Read and write files using the built-in Python file methods
# LinkedIn Learning Python course by Joe Marini
#

    
# Open the file and read the contents
file = open("./Start/Ch6/textfile.txt","r")
if file.mode == "r":
  # use the read() function to read the entire file
  contents = file.read()
  print(contents)

  file_lines = file.readlines()
  for txt in file_lines:
    print(txt)

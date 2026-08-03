# LinkedIn Learning Python course by Joe Marini
# write files using the built-in Python file methods
#


# Open a file for writing and create it if it doesn't exist
file = open("./Start/Ch6/textfile.txt","w+")
file.write("a text. hello world!")
file.close()


# Open the file for appending text to the end
file = open("./Start/Ch6/textfile.txt","a+")
file.write("another text. hello world!")


# write some lines of data to the file
file.write("chapter 6.")

# close the file when done
file.close()
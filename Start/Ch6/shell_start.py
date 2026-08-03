#
# Example file for working with filesystem shell methods
# LinkedIn Learning Python course by Joe Marini
#
import os
from os import path
import shutil

from zipfile import ZipFile

# make a duplicate of an existing file
if path.exists("./Start/Ch6/textfile.txt"):
    # get the path to the file in the current directory
    file = path.realpath("./Start/Ch6/textfile.txt")
        
    # # let's make a backup copy by appending "bak" to the name
    dst = file + ".bak"

    # # now use the shell to make a copy of the file
    shutil.copy(file,dst) #no metadata
    shutil.copy2(file,dst) #with metadata

    # # rename the original file
    os.rename("./Start/Ch6/textfile.txt","./Start/Ch6/textfile2.txt")
    os.rename("./Start/Ch6/textfile2.txt","./Start/Ch6/textfile.txt")
    
    # now put things into a ZIP archive
    root_dir,tail = path.split(file)
    #print(root_dir)
    shutil.make_archive("archive","zip",root_dir)


    # more fine-grained control over ZIP files
    with ZipFile("./Start/Ch6/test.zip","w") as newzip:
        newzip.write("./Start/Ch6/textfile.txt")
        newzip.write("./Start/Ch6/textfile.txt.bak")

    # newzip2 = ZipFile("./Start/Ch6/test.zip","w")
    # newzip2.write("./Start/Ch6/textfile.txt")
    # newzip2.write("./Start/Ch6/textfile.txt.bak")
    # newzip2.close()
    
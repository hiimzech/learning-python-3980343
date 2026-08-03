# LinkedIn Learning Python course by Joe Marini
# Example file for parsing and processing XML
#

import xml.dom.minidom as xml

# use the parse() function to load and parse an XML file

data = xml.parse("./Start/Ch7/samplexml.xml")

# print out the document node and the name of the first child tag

print(data.nodeName)
print(data.firstChild.nodeName)

# get a list of XML tags from the document and print each one

def printskills():
  skills = data.getElementsByTagName("skill")
  print(f"Number of skills: {skills.length}")

  for x in skills:  
    print(x.getAttribute("name"))

printskills()    

# create a new XML tag and add it into the document
nskill = data.createElement("skill")
nskill.setAttribute("name","reactjs")
data.firstChild.appendChild(nskill)

printskills()


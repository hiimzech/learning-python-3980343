# LinkedIn Learning Python course by Joe Marini
# Example file for parsing and processing JSON
#

import json
import urllib.request 

# Open the URL and read the data
url = urllib.request.urlopen("http://uselessfacts.jsph.pl/api/v2/facts/random")
print(f"result code: {url.getcode()}")

# Read the JSON data from the source
data = url.read()
print(data)
json_data = json.loads(data)

# Print the content of the 'text' field
print(json_data["text"])
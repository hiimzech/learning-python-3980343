# LinkedIn Learning Python course by Joe Marini
# Example file for retrieving data from the internet
#

import urllib.request

url = urllib.request.urlopen("http://www.example.com")

print(f"result code: {url.getcode()}")

data = url.read()
print(data)
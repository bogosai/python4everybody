
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter link - ')
ipos = input('Position - ')
nbD = input('Number of drills - ')
nbDrills = int(nbD)
iposition = int(ipos)

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('a')
print(url)
index = 1
position = 1
while index <= nbDrills:
    for tag in tags:        
        if position == iposition:                     
            print(tag.contents[0])
            url = tag.get('href', None)            
            html = urllib.request.urlopen(url, context=ctx).read()            
            soup = BeautifulSoup(html, "html.parser")            
            tags = soup('a')            
        position = position + 1
    position = 1
    index = index + 1

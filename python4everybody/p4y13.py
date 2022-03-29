
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as et
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sourcexml = urllib.request.urlopen(input('provide URL: '), context=ctx).read()
commentinfo = et.fromstring(sourcexml)
lst = commentinfo.findall('comments/comment')

total = 0
for item in lst:
    total = total + int(item.find('count').text)
print(total)
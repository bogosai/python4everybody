import json

import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sourcejson = urllib.request.urlopen(input('provide URL: '), context=ctx).read()

info = json.loads(sourcejson)
print('User count:', len(info['comments']))
total = 0
for item in info['comments']:
    total = total + int(item['count'])
print(total)   
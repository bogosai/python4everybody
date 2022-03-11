import re
txt = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
test = re.findall("\S+@\S+",txt)
print(test)


x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)
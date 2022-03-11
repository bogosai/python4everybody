name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fn = open(name)
hours = dict()

for ln in fn:
    line = ln.strip()
    if not 'From ' in line:continue
    lst = line.split()
    fulltime = lst[5]
    sfulltime = fulltime.split(':')
    hourvalue = sfulltime[0]
    hours[hourvalue] = hours.get(hourvalue, 0) + 1
thours = sorted(hours.items())
for k,v in thours:
    print(k,v)

#popularity = None
#person = None
#for k, v in efreq.items():
    #if popularity is None or v > popularity:
     #   popularity = v
      #  person = k
#print(person, popularity)
#print(efreq)

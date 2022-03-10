name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fn = open(name)
efreq = dict()
for ln in fn:
    line = ln.strip()
    if not 'From ' in line:continue
    lst = line.split()
    email = lst[1]
    efreq[lst[1]] = efreq.get(lst[1],0) + 1
popularity = None
person = None
for k, v in efreq.items():
    if popularity is None or v > popularity:
        popularity = v
        person = k
print(person, popularity)
#print(efreq)

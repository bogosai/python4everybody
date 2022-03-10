fn = input("Enter file name: ")

try:
    fname = open(fn)
except:
    print("cannot find file")
    quit()
count = 0
for ln in fname:
    line = ln.strip()
    if not 'From ' in line:continue
    sline = line.split()
    count = count + 1
    print(sline[1])
print("There were", count, "lines in the file with From as the first word")

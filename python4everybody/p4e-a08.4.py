fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for ln in fh:
    line = ln.rstrip()
    lnlst = line.split()    
    for miniitem in lnlst:        
        if miniitem in lst:continue
        lst.append(miniitem)
lst.sort()
print(lst)


    
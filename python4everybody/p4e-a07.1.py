# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for li in fh:
    ln = li.rstrip()
    print(ln.upper())
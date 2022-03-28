import re

name = input("Enter file:")
if len(name) < 1:
    name = "regex_sum_1501879.txt"
    #name = open("test11.txt")
    #name = open("regex_sum_42.txt")
handle = open(name)

numbers = list()
result = 0
for ln in handle:
    line = ln.strip()
    numbers = re.findall("[0-9]+",line)
    if len(numbers) < 1 : continue
    #print(len(numbers))
    i = 1
    while i <= len(numbers):
        value = int(numbers[i - 1])
        result = result + value
        i = i + 1
print(result)
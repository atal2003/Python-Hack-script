#! /usr/bin/python3


fname = input("enter a file name: ")
tfile = open(fname)


counts = dict()
for line in tfile:
    line = line.rstrip() # will get rid of white space on the right side of page. 
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
#print(counts)


largest = -1 
theword = None 
for k, v in counts.items():
    if v > largest:
        largest = v
        theword = k

print(theword, largest)


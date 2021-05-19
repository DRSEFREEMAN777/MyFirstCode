infile = open("abstract.txt", "r")
   
content = []

plist = infile.readline()
while plist:
    content.append(plist)
    plist = infile.readline()

infile.close()

content2 = []

for elem in content:
    elem2 = elem.lower()
    content2.append(elem2)

outfile = open("Abstract.txt", "w")

for elem3 in content2:
    outfile.write(elem3 + '\n')


outfile.close()

#code challenge make list for numbers 
infile = open("NumbersString", "r")
   
content = []

plist = infile.readline()
while plist:
    content.append(plist)
    plist = infile.readline()

infile.close()

content2 = []

for elem in content:
    elem2 = elem.lower()
    content2.append(elem2)

outfile = open("NumbersString", "w")

for elem3 in content2:
    outfile.write(elem3 + '\n')


outfile.close()

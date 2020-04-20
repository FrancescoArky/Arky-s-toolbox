file = open("GPL96-15653.txt")
listwords = ["cancer", "diabetes", "disease", "neuropathy"]

nf = open("nf.txt", 'w')

for row in file:
    for word in listwords:
        temp = row.split()
        if row[0] == "#" or row[0:2] == "ID":
            pass
        elif word in row:
            i = row.find(word)
            #nf.write(temp[0] + " " + row[i - 4] + " " + row[i - 3] + " " + row[i - 2] + " " + row[i - 1] + " " + row[i] + " " + row[i + 1] + " " + row[i + 2])
            nf.write(temp[0] + " " + row[i-25:i+len(word)+16] + "\n")
        else:
            nf.write(temp[0] + " None\n")
print ("Name: Hunter Hanson")

#Defining the variables
total = 0
word1 = "gmeach18@ed.gov"
word2 = "248.253.63.149"
word3 = "Whiteland"
word4 = "80.222.19.190"
word5 = "Kayley"
word6 = "dcassyqw@microsoft.com"

#Checking lines for keywords and adding their line number
#to the total count
with open('Midterm-if.txt','r') as hFile:
    for number, line in enumerate(hFile):
        if word1 in line:
            print (line)
            total += number
        elif word2 in line:
            print (line)
            total += number
        elif word3 in line:
            print (line)
            total += number
        elif word4 in line:
            print (line)
            total += number
        elif word5 in line:
            print (line)
            total += number
        elif word6 in line:
            print (line)
            total += number
#Printing the final total
print (f"The total is:{total}")

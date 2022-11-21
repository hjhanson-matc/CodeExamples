print ("Name: Hunter Hanson")

#Accessing the file
hFile = open('slicing-file.txt','r')
filelines = hFile.readlines()
slicingfile = " ".join(filelines)
slicingfile = slicingfile.split()
hFile.close()
#Setting up variables

word1 = slicingfile[-3]
word2 = slicingfile[2:5]
word2 = " ".join(word2)
word3 = slicingfile[-10:-16:-2]
word3 = " ".join(word3)
word4 = slicingfile[10:13]
word4 = " ".join(word4)
word5 = slicingfile[-19:-22:-1]
word5 = " ".join(word5)


#Adding the words to new string

quote = f"{word1} {word2} {word3} {word4} {word5}"


print (quote)


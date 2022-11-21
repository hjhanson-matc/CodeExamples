#Hunter Hanson
#This script copys the passwd file to a new file.

#Question 1
#aFile = open("/etc/passwd",'r')

#indata = aFile.read()

#to_file = ("passwd_str.txt")
#out_file = open(to_file, 'w')
#out_file.write(indata)
#out_file.close()

#bFile = open("passwd_str.txt",'r')
#strPasswd = bFile.read()

#print (f"The copied file is {len(strPasswd)} bytes long")
#print ("This length includes all unicode characters, including line breaks.")
#print ("You would use this read function over others when you want to work with entire documents,")
#print ("it works best with short documents.")


#bFile.close()
#aFile.close()


#Question 2
aFile = open("/etc/passwd", 'r')

indata = aFile.readlines()

to_file = ("passwd_list.txt")
out_file = open(to_file, 'w')
out_file.writelines(indata)
out_file.close()

aFile.close()

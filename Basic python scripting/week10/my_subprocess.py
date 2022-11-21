#Hunter Hanson

#Import the module
import subprocess

#Call the command
myProc = subprocess.run(['ps','-axco','command'],stdout=subprocess.PIPE)

#Decode the information
myProcString = myProc.stdout.decode()

#Split into a list
myProcList = myProcString.split('\n')

#Print to the screen one by one
for line in myProcList:
    print (line)

#Count the number of lines
#   First slice off the field header
myProcList = myProcList[1::]

print (f"There are {len(myProcList)} processes")

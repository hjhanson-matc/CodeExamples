#python scriping week4 assignment
#Hunter Hanson


varString = "Here is a nice string to slice"
varList = ["Here", "is", "a", "nice", "list", "to", "slice"]

#2a
print (f"{varString[3::]: <0s}")
#2b
print (f"{varString[:3:]: <0s}")
#2c
print (f"{varString[3:12:]: <0s}")
#2d
print (f"{varString[::2]}")
#2e
print (f"{varString[::-1]: <0s}")
#3a
print (f"{varList[::-1]}")
#3b
print (f"{varList[2::-1]}")
#3c
print (f"{varList[2:4:]}")
#3d
print (f"{varList[::3]}")
#3e
print (f"{varList[1::]}")
#4
for string in varString:
    print (f"{string}")
#5
for list in varList:
    print (f"{list}")

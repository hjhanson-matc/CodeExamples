#Hunter Hanson, tempconversion

#First, print what the script does
print ("Ready to convert the tempurture?")

#Then we get the tempurture and measure from user
tempurture = float(input("Enter the tempurture > "))

measure = input("Is this tempurture in fahrenheit (f) or celcius (c)?\n->")

#Now we run the calculations

if measure in ["f", "fahrenheit"]:
    from f2c import multiply, subtract
    tempurture = multiply(subtract(tempurture))
    tempurture = round(tempurture, 3)
    print (f"The tempurture is {tempurture} degrees celsius.")

elif measure in ["c", "celcius"]:
    from c2f import multiply, add
    tempurture = add(multiply(tempurture))
    tempurture = round(tempurture, 3)
    print (f"the tempurture is {tempurture} degrees fahrenheit.")

else:
    print (f"Unknown measurement")

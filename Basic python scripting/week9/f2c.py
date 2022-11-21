#Hunter Hanson, f2c

#First, create the functions
def subtract(a):
    return a - 32

def multiply(a):
    return a * 5 / 9

#Need to make a main function so we can import the other functions without
#importing the rest of the code
def main():
#Next, get the user input for fahrenheit
    tempurture_f = float(input("What is the tempurture in fahrenheit:"))

#Do the fahrenheit to celsius calculations
    tempurture_c = multiply(subtract(tempurture_f))

#Round to 3 decimals so it looks nice
    tempurture_c = round(tempurture_c, 3)

#finally print the tempurture in celsius
    print (f"The tempurture in celsius is: {tempurture_c}")

if __name__ == "__main__":
    main()

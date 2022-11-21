#Hunter Hanson, c2f

#First, get the functions set up
def multiply(a):
    return a * 9 / 5

def add(a):
    return a + 32

#Make a main function so I can import the multiply and add functions but
#not the rest of the script
def main():
#Next, I need to get the tempurture in celsius from the user
    tempurture_c = float(input("What is the tempurture in celsius:"))

#Time to do the calculations
    tempurture_f = add(multiply(tempurture_c))

#Round to 3 decimals so it looks nice
    tempurture_f = round(tempurture_f, 2)

#Print the result
    print (f"the tempurture in fahrenheit is: {tempurture_f}")

if __name__ == "__main__":
    main()

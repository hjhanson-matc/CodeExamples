print ("Name: Hunter Hanson")

#Initalizing dictionarys
password_database = {'Username' : 'dnedry','Password' : 'please'}
command_database = {
'reboot' : 'OK. I will reboot all park systems.',
'shutdown' : 'OK. I will shut down all park systems.',
'done' : 'I hate all this hacker stuff.'
}

#Initalizing objects
white_rabbit_object = 0
counter = 0

#Creating the while loop
while white_rabbit_object == 0:
    input_user = input("Enter Username:")
    input_password = input("Enter Password:")
    if input_user in password_database.get('Username'):
        if input_password in password_database.get('Password'):
            white_rabbit_object = 1
        elif counter < 2:
            counter += 1
            print (f"You didn't say the magic word. {counter}")
        else:
            print (f"You didn't say the magic word!\n" * 25 )
            quit()
    elif counter < 2:
        counter += 1
        print (f"You didn't say the magic word. {counter}")
    else:
        print (f"You didn't say the magic word!\n" * 25)
        quit()
#After a correct login
else:
    print ("\nHi, Dennis. You're still the best hacker in Jurassic Park.")

command = input(f"Enter a command\n(available commmands are {command_database.keys()})\n--->")

if command == "reboot":
    print (command_database['reboot'])
elif command == "shutdown":
    print (command_database['shutdown'])
elif command == "done":
    print (command_database['done'])
else:
    print ("The Lysine Contingency has been put into effect.")

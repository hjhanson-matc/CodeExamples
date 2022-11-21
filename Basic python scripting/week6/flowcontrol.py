#Hunter Hanson

print ("""The cave you stepped into is dark, but with the faint light of your torch
you can see 3 tunnels ahead of you. \nWill you take tunnel 1, tunnel 2, or tunnel 3?""")

path = input("-> ")

#Path 1 logic
if path == '1':

    print ("As you enter the tunnel you see a faint orange glow ahead.")
    print ("What would you like to do?\n")

    print ("1. Contine down the tunnel")
    print ("2. Turn back toward the entrance")

    #Glow logic
    glow = input ("-> ")

    if glow == "1":
        print ("""You get closer to the glow and realize it is the glow of magic, but
you notice too late and your body becomes well acquainted with a fireball.\n\nYou Died.""")
    elif glow == "2":
        print ("""As you turn back to the entrance you are face to face with a skeletal figure
and feel a sharp pain in your stomach, he stabbed you.\n\nYou Died.""")
    else:
        print ("""You stand still, frozen in fear as the glow dims and then disappears. I think
it's time to leave.\n\nYou Go Home""")

#Path 2 logic
elif path == "2":
    print ("""You walk down the tunnel for a while until you come to a large opening with a hole
in the middle.""")

    print ("1. Approach the hole.")
    print ("2. Go around the hole to the back of the room.")
    print ("3. Turn back toward the entrance.")

    #Hole logic
    hole = input ("-> ")

    if hole == "1":
        print ("You approach the hole and see that it looks deep.")

        print ("1. Peek over the edge.")
        print ("2. Back away from the hole.")
        print ("3. Dive into the hole.")

        #Peek logic
        peek = input ("-> ")

        if peek == "1" or peek == "2":
            print ("You feel a light shove on your back as you go tumbling down the hole.\n\nYou Died")
        elif peek == "3":
            print ("Yo-- what, I mean *cough* \nYou dive down the hole and snap your neck.\n\nYou Died")
        else:
            print ("The entire floor disappears. It must have been magic!\n\nYou Died")

    elif hole == "2":
        print ("""As you go around the back of the room you see something sparkling, you found a
gold necklace inlaid with emerald, this must be worth a fortune!\n\nGood Job""")

    elif hole == "3":
        print ("""You turn around to leave as the whole room collapses and you get crushed under
the falling rubble.\n\nYou Died""")

    else:
        print ("""You hear a loud bang as the entire room gets enveloped in fire and you
instantly get disintegrated by the sheer force of the explosion.\n\nYou Died""")

#Path 3 logic
elif path == "3":
    print ("""You only get a few steps into the tunnel before you hear heavy footsteps thumping
toward you.""")

    print ("1. Draw your sword and prepare for a fight.")
    print ("2. Turn around and run for the entrance.")
    print ("3. Attempt to hide in the shadows.")

    #Encounter logic
    encounter = input("-> ")

    if encounter == "1":
        print ("""You draw your sword in preperation for a fight, but as the figure gets closer
you lock eyes with it, it's a demon. The demon rushes forward with a speed you couldn't
follow with your human eyes. Before you could even raise your sword, your head is falling to the
floor.\n\nYou Died""")
    elif encounter == "2":
        print ("""You turn around and run towards the entrance. You get out of the cave safely and
decide that you might be better off going back home.\n\nYou Ran Away""")
    elif encounter == "3":
        print ("""You hide in the shadows, as the figure rounds the edge of the tunnel you notice
it's a demon. wait... THEY CAN SEE IN THE DARK!! The food chain commences.\n\nYou Died""")

else:
    print ("Why are you even here?\n\nYou Go Home")

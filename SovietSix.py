def bloc():
    print("VENERA")
    print(" ")
    print("You are standing in a barren room with a light layer of dust spread on the floor. There is a small table with a envelope on it and a small photograph underneath a cracked window. There is an overturned chair nearby. There is a small calander on the wall to your right.")
    print("What do you wish to do?: ")
    print(" ")
    print("1. Read Calander: ")
    print("2. Examine Photograph: ")
    print("3. Examine envelope: ")
    print(" ")
    playerChoice = input(">>>")

    if playerChoice == "1":
        print("September the 23rd, 1990")
    elif playerChoice == "2":
        print("Depicts an unknown person standing in a dark alley, no further details can be made out.")
    elif playerChoice == "3":
        print("Severly yellowed and brittle with no recipient, fairly heafty in weight.")

    else:
        print("You have committed an error. Please try again")
        bloc()

def ExitBloc(): 
    print(" ")
    print("You hear a knock at the door. They are here.")
    print(" ")
    print("What do you wish to do?: ")
    print(" ")
    print("1. Climb out the window. ")
    print("2. Answer the door ")
    print("3. Wait here. After all patience is the key to victory in some cases.")
    print(" ")

    playerChoice = input(">>>")

    if playerChoice == "1":
        print("The window was easy to open. Grabbing your things, you quickly climb out into the side street below.")
    elif playerChoice == "2":
        print("You are dragged to the ground and a hood is placed over your head.")
        print(" ")
        print("GAME OVER")
        bloc()
    elif playerChoice == "3":
        print("The door is busted open. You are dragged to the ground and a hood is placed over your head.")
        print(" ")
        print("GAME OVER")
        bloc()
    else:
        print("You have committed an error. Retry again")
        ExitBloc()

def SideStreet(): 
    print(" ")
    print("It is dusk. The sidestreet is riddled with long shadows in all directions. There is a side alley branching off to the right into the thick shadows and a clear path straight ahead.")
    print(" ")
    print("What do you wish to do?: ")
    print(" ")
    print("1.  Follow the side street")
    print("2.  Duck into the side alley")
    print(" ")

    playerChoice = input(">>>")

    if playerChoice == "1":
        print("The side street leads to the main road where there is no one else around at this hour. There is a lone car parked on the street with one of the windows down.")
    elif playerChoice == "2":
        print("The side alley is small and dark. It abruptly ends after several feet. You hear the sound of voices and boots behind you and you duck behind several dustbins as they pass in the direction of the main street.")
        print(" ")
        sideAlley()

    else:
        print("You have committed an error. Retry again")
        SideStreet()

def MainRoad(): 
    print(" ")
    print("The main road is deserted. Save for one car with the windows down. There is a manhole nearby. The sound of rapid footsteps approaches.")
    print(" ")
    print("What do you wish to do?: ")
    print(" ")
    print("1.  Duck into the car")
    print("2.  Enter the manhole")
    print("3. Wait here. After all patience is the key to victory in some ways.")
    print(" ")

    playerChoice = input(">>>")

    if playerChoice == "1":
        print("You quickly reach through the windows and unlock the car. Ducking down in the footwell as the voices grow closer.")
        ladaStreet()
    elif playerChoice == "2":
        print("You scurry down the manhole as the voices grow nearer. The area is only faintly lit by the light from above. A tunnel continues to the left where it is darker. There is a small toolbox here.")
        print(" ")
        undergroundAccess()
    else:
        print("You have committed an error. Retry again")
        MainRoad()


def undergroundAccess():
    print(" ")
    print("There is a small toolbox nearby. The tunnel to the left is pitch black. Better find a light source.")
    print(" ")
    print("What do you wish to do?: ")
    print(" ")
    print("1.  Go back up the manhole")
    print("2.  Check the toolbox")
    print("3. Wait here. After all patience is the key to victory in some ways.")
    print(" ")

    playerChoice = input(">>>")

    if playerChoice == "1":
        gameOverGeneral()

    elif playerChoice == "2":
        print("You search the toolbox and find an old but usable torch, the bulb flickers slightly as you move down the tunnel.")
        print(" ")
        tunnel()
    elif playerChoice == "3":
        print("Frankly this is gonna take a while. You wait for what seems like an hour seeing no change in the situation at hand.")
        undergroundAccess()

    else:
        print("You have committed an error. Retry again")
        undergroundAccess()


def sideAlley(): 
    print(" ")
    print("There is no other routes out of the side alley save for one door next to you.")
    print(" ")
    print("What do you wish to do?: ")
    print(" ")
    print("1. Try the door.")
    print("2. Go back to the Side Street")
    print("3. Wait here. After all patience is the key to victory in some ways.")
    print(" ")

    playerChoice = input(">>>")

    if playerChoice == "1":
        print("The door is slighty jammed but with some effort you get it open. The room it leads to is suprisingly well lit. There is a person sitting in a chair in the middle of the room staring intensly at you.")
        theOddOne()

    elif playerChoice == "2":
        gameOverGeneral()

    elif playerChoice == "3":
        gameOverGeneral()

    else:
        print("You have committed an error. Retry again")
        sideAlley()
    

def gameOverGeneral():
    print(" ")
    print("They are everywhere. You are forced to the ground and a hood is placed over your head.")
    print(" ")
    print("GAME OVER")
    bloc()

def theOddOne():
    print(" ")
    print("The person in the chair continues their undending stare. 'Late. 4 days 23 hours 51 seconds' the voice raspily states.")
    print(" ")
    print("What do you wish to do?: ")
    print(" ")
    print("1. Respond with 'I'm sorry?' ")
    print("2. Respond with 'Who are you?' ")
    print("3. Respond with an intense stare back at them. After all two can play at this game.")
    print("4. Wait here. After all this isn't exactly the least justified response all things considered.")
    print(" ")

    playerChoice = input(">>>")

    if playerChoice == "1":
        print("The person in the chair tilts their head slightly and smiles. 'Browsing. They will not rest. '")
        theOddOne()
    elif playerChoice == "2":
        print("The person in the chair closes their eyes and their expression changes to one of fustration. Suddenly the lights in the room flicker and the person vanishes. You leave through the door opposite the room.")
        theLastLaugh()

    elif playerChoice == "3":
        print("The person in the chair stares back. Never blinking. The room around you begins to sway and objects move around. Suddenly the lights go out and the world seems to vanish beneath you.")
        print(" ")
        print("GAME OVER")
        bloc()
    elif playerChoice == "4":
        print("The person in the chair continues to stare at you and you ingnore them. Hours pass and the situation doesn't change much.")
        theOddOne()
    else:
        print("You have committed an error. Retry again")
        theOddOne()

def theLastLaugh():
    print(" ")
    print("This door leads to a long corridor that seems to loop endlessly. You follow it until the end.")
    print(" ")
    print("GAME OVER")
    bloc()

def tunnel():
    print(" ")
    print("The tunnel seems to get smaller and smaller until it becomes untraversable. You try to turn around and realize that the tunnel is shrinking. A screech is heard before the world turns black.")
    print(" ")
    print("GAME OVER")
    bloc()
    

bloc()
ExitBloc()
SideStreet()




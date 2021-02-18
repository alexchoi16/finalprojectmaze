import cmd
import textwrap
import sys
import random
import time 

#Meat part of the game --------------------------------------------------------------------------------------------------------------
AREA =  " "
DESCRIPTION = "description"
visited = False
LEFT = "left" , "west"
RIGHT = "right" , "east"

#Dictionary for cleared places 
cplace = {"cavea0": False,"caveb0": False,"cavec0":False,
            "cavea1": False,"caveb1": False,"cavec1":False,
            "cavea2": False,"caveb2": False,"cavec2":False,
        }

#Dictionarys for the description of each location of the cave
details = {
    "cavea0": {
        AREA: "Cave 1" ,
        DESCRIPTION: "This is starting cave 1",
        visited : False,
        LEFT : "caveb0",
        RIGHT : "cavea1" ,
        },  
    "cavea1": {
        AREA : "Start",
        DESCRIPTION : "This is the starting point entrance",
        visited : False,
        LEFT : "cavea0",
        RIGHT : "cavea2" ,
    },
    "cavea2": {
        AREA : "cave 2",
        DESCRIPTION : "This is starting cave point 2",
        visited : False,
        LEFT : "cavea1",
        RIGHT : "caveb2" ,
    },  
    "caveb0": {
        AREA : "Cave 1b",
        DESCRIPTION : "This is the next cave near the starting cave 1",
        visited : False,
        LEFT : "cavec0",
        RIGHT : "cavea0" ,
    },          
    "caveb1": {
        AREA : "MYSTERY",
        DESCRIPTION : "MYSTERY Cave",
        visited : False,
        LEFT : "cavea1",
        RIGHT : "cavec1" ,
    },  
    "caveb2": {
        AREA : "Cave 2b",
        DESCRIPTION : "This is the next cave near the starting cave 2",
        visited : False,
        LEFT : "cavea2",
        RIGHT : "cavec2" ,
    },  
    "cavec0": {
        AREA : "Cave 1c",
        DESCRIPTION : "This is the left corner cave that may lead to the exit",
        visited : False,
        LEFT : "cavec1",
        RIGHT : "caveb0" ,
    },  
    "cavec1": {
        AREA : "Exit",
        DESCRIPTION : "This is the exit ",
        visited : False,
        LEFT : "cavec0",
        RIGHT : "cavec2" ,
    },  
    "cavec2": {
        AREA : "Cave 2c",
        DESCRIPTION : "This is the right hand corner cave that may lead to the exit",
        visited : False,
        LEFT : "cavec1",
        RIGHT : "caveb2" ,
    } 
    
}
#user information -----------------------------------------------------------------------------------------------------------------
class Puser:
    def __init__(self):
        self.name = ""
        self.location = "cavea1"
        self.lost = False

    def ask_player_name(self):
        self.name = input("What is your name? \n")
        delay()
        print ("AH, I remember now, my name is " + self.name )

the_user = Puser() 

#This is the game conditions for the loading screen 
def screen_option():
    option = input(">")
    if option.lower() == ("play"):
        storyline()
    elif option.lower() == ("quit"):
        sys.exit()
    while option not in ["play","quit"]:
        print ("Invalid Option, Please enter the Option.")
        option = input(">")
        if option.lower() == ("play"):
            storyline()
        elif option.lower() == ("quit"):
            sys.exit()

#This is the loading screen/ Menu 
def opening_screen():
    print ("Welcome to my RPG game")
    print ("        -Play-        ")
    print ("        -Quit-        ")
    screen_option()

#--------------------------------------------------------------------------------------------------------------------------------------------
#Printing out the current location of the User/ Player
def print_currentloc():
    print (">" + the_user.location + "<")
    print (">" + details[the_user.location][DESCRIPTION])
    user_exit()


#Prompts the user and ask where they want to go --------------------------------------------------------------------------------------------------------------
def statement():
    
    print("The only routes you can take is either the left cave entrance or the right cave entrance.\n Do you want to go Left or Right ?")
    movement = input(">")
    onlystatement = ["left","right","quit"]
    while movement.lower() not in onlystatement:
        print ("I'm not sure what you mean.\nDo you want to go Left or Right?\n")
        movement = input(">")

    if movement.lower() in ["left","right"]:
        user_movement(movement.lower())
    elif movement.lower() in ["quit"]:
        sys.exit()    
    else:
        print ("Invalid movement")
        movement = input(">")
        if movement.lower() in ["left","right"]:
            user_movement(movement.lower())
        else:
            print ("Invalid movement")

def user_movement(action):
    if action in ["left" , "west"]:
        room = details[the_user.location][LEFT]
        functional_move(room)
    elif action in ["right" , "east"]:
        room = details[the_user.location][RIGHT]
        functional_move(room)

#This will print out the location that the user is at and set its location ------------------------------------------------------------------------------
def functional_move(room):
    print("\n" + "You arrived to at " + room + ".")
    the_user.location  = room
    print_currentloc()   

#This is the conditional statement in which users will see a statement if they visited the room before or not ----------------------------------------------
def user_look():
    if details [the_user.location][visited] == True:
        print ("You have been here before ")
    else:
        print ("This place looks new")
        details [the_user.location][visited] = True

#this is the exit prommpt that users will receive once they reach the exit cave room -------------------------------------------------------------------    
def user_exit(): 
    if the_user.location == "cavec1":
      print (">" + the_user.name + ", you have reached the end of the cave, well done on surviving")
      print("---------------")
      print("   GAME OVER   ")
      print("---------------")
      sys.exit() 
    else :
      user_look()
    

#main loop so that game continues------------------------------------------------------------------------------
def main_loop():
    while the_user.lost == False:
        statement()

#Timer delay so that the text isn't instant-------------------------------------------------------------------------------------------------------------------------
def delay():
    time.sleep(0.5)
#Story Line-------------------------------------------------------------------------------------------------------------------------
def storyline():

    print("Welcome to Escape the Cave")
    delay()
    print("As you start to wake up \nYou realize that you are inside an unknown cave with no recollection of how you got there")
    delay()
    print("With only a flashlight next to you with no food or water \nYou start trying to remember your name")
    delay()
    the_user.ask_player_name()
    startpoint()

#Start of adventure ------------------------------------------------------------------------------------------------------------------
def startpoint():
    start_choice = ""
    print( "As you start to get yourself up \nYou realize that the only direction you can go is forward")
    start_choice = input("Do you want to venture forward or stay?\n")

    if start_choice == "stay":
        print("You decided to stay where you were and later died due to malnourishment and dehydration")
        print("Nobody will remember who you are \nAll because you decided not to go forward and attempt survival")
        print("---------------")
        print("   GAME OVER   ")
        print("---------------")
        quit()
        
    elif start_choice == "move forward":
        print("You have decided to move forward and venture onwards further deep inside the cave")

    main_loop()

'''
MAP LOCATION
---------------------------
|       |         |       |  
|  c0   |   c1    |  c2   |  
---------------------------
|       |         |       |  
| b0    |   b1    |   b2  |  
---------------------------
|       |         |       |  
| a0    |   a1    |   a2  |  
---------------------------
'''
opening_screen()

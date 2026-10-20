import time
import random
import sys
from playsound import playsound

xp = 0
pumpkins = 0
XP_BOOST = 2
MIDNIGHT_BOOST = 5
start_system_confirmed = False
name = ""


def game_start(start_system_confirmed):
    print("For best experience, please set audio to 60%. ")
    name = input("Welcome to the adventure, what is your name explorer? ")
    time.sleep(0.5)
    print(f"Welcome {name}, it's great to meet you - my name is Barry...")
    time.sleep(1)
    while start_system_confirmed == False:
        start_system = input("Are you ready to start? (yes/no) ")
        if start_system.lower().strip() ==  "yes" or start_system.lower().strip() == "y":
            print("Loading your game now")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...")
            start_system_confirmed = True
            forest()

        elif start_system.lower().strip() ==  "no" or start_system.lower().strip() == "n":
                    print(f"See you soon {name}")
                    playsound('death.mp3', block=False)
                    death(name)
        
        else:
            print("Please enter yes or no. ")
            start_system_confirmed = False

    return name


def forest():
    print("Slowly you step...")
    time.sleep(1.5)
    print("Up above lays and old sign, WELCOME TO THE FOREST")
    time.sleep(2)
    playsound('scream.wav')
    time.sleep(0.5)
    print("Did you hear that? It sounded like it was deep in the forest.")
    choicemade = False
    while choicemade == False:
        time.sleep(0.5)
        forest_choice_one = input("Do you want to go deeper into the forest or leave? (deeper/leave) ")
        try:
            if forest_choice_one == "deeper":




                choicemade = True
            elif forest_choice_one == "leave":





                choicemade = True
        except:
            print("You are too far in, you can only go deeper or leave. (deeper/leave)")
            choicemade = False

def old_hotel():
    print("Old Hotel")

def bedroom():
    print("Bedroom.")

def nursery():
    print("Nursery.")

def graveyard():
    print("Graveyard.")

def death(name):
    playsound('death.mp3', block=False)
    time.sleep(4)
    print(f"{name} died with {xp} experience points. ")
    sys.exit()

name = game_start(start_system_confirmed)


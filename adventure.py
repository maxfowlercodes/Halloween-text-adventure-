import time
import random
import sys
from playsound import playsound

xp = 0
pumpkins = 0
XP_BOOST = 2
MIDNIGHT_BOOST = 5
start_system_confirmed = False


def game_start(start_system_confirmed):
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

        elif start_system.lower().strip() ==  "no" or start_system.lower().strip() == "n":
                    print(f"See you soon {name}")
                    playsound('death.mp3', block=False)
                    time.sleep(7)
                    print(f"{name} died before even starting the game. ")
                    sys.exit()
        
        else:
            print("Please enter yes or no. ")
            start_system_confirmed = False


def forest():
    print("Forest.")

def old_hotel():
    print("Old Hotel")

def bedroom():
    print("Bedroom.")

def nursery():
    print("Nursery.")

def graveyard():
    print("Graveyard.")

game_start(start_system_confirmed)
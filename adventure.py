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
    print("For best experience, please set audio to 60%. For each question answered you get a random amount of XP 1-20. ")
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
            forest(xp, name)

        elif start_system.lower().strip() ==  "no" or start_system.lower().strip() == "n":
                    print(f"See you soon {name}")
                    playsound('death.mp3', block=False)
                    death(name)
        
        else:
            print("Please enter yes or no. ")
            start_system_confirmed = False

    return name


def forest(xp, name):
    print("Slowly you step...")
    time.sleep(1.5)
    print("Up above lays and old sign, WELCOME TO THE FOREST")
    time.sleep(2)
    playsound('scream.wav')
    time.sleep(0.2)
    print("Did you hear that? It sounded like it was deep in the forest.")
    forest_choices_made = False
    while forest_choices_made == False:
        time.sleep(0.5)
        print()
        forest_choice_one = input("Do you want to go deeper into the forest or leave? (deeper/leave) ")
        if forest_choice_one.strip().lower() == "deeper":
            print()
            xp = xp + random.randint(1,20)
            print(f"{name} creeps deeper into the forest...")
            time.sleep(1)
            print("The path is rocky, very jagged and rough...")
            time.sleep(1)
            print("You keep your head down, walking anyway.")
            time.sleep(5)
            print("Out of the corner of your eye, you see a glowing pulse under a large rock...")
            print()
            forest_choices_made = False
            while forest_choices_made == False:
                forest_choice_two = input("Do you go an lift the rock up? (yes/no) ")
                if forest_choice_two.strip().lower() == "yes" or forest_choice_two.strip().lower() == "y":
                    print()
                    xp = xp + random.randint(1,20)
                    print("You walk over towards the rock.")
                    time.sleep(0.5)
                    print("This rock is heavy, you can lift it up with some help. A forest goblin can help you for XP.")
                    time.sleep(1)
                    print("The cost is your choice, but if you offer to low... you may be punished.")
                    time.sleep(1)
                    xp_question_one =  int(input(f"You currently have {xp} XP - enter how much you offer to the goblin. "))
                    if xp_question_one >= 20 and xp >= xp_question_one:
                        print("The golbin accepts your offer.")
                        xp = xp - xp_question_one
                        print(f"You now have {xp} XP.")
                        time.sleep(1)
                    elif xp_question_one >= 20:
                        print("The goblin did accept your offer, but you did not have enough to pay them.")
                        death(name, xp)
                    else:
                        print("The goblin did not accept your offer...")
                        death(name, xp)

                    time.sleep(0.5)
                    extra_xp = random.randint(20,50)
                    print(f"Under the rock lays a potion, this has granted you {extra_xp}XP bonus.")
                    xp = xp + extra_xp



                print("You continue walking past the rock... ")
                time.sleep(1)



                print()
                print("You keep walking, and see a building outline.")
                print()
                time.sleep(1)
                forest_choice_three = input("Do you walk towards it or keep moving? (towards/continue) ")
                if forest_choice_three.lower().strip() == "towards" or forest_choice_three.lower().strip() == "t":
                    xp = xp + random.randint(1,20)
                    print("You walk towards the building, lit with old lights flickering...")
                    old_hotel(name, xp, forest_choices_made)

                elif forest_choice_three.lower().strip() == "continue" or forest_choice_three.lower().strip() == "c":
                
                    xp = xp + random.randint(1,20)
                    print("You continue walking past the old building.")
                    time.sleep(0.5)
                    print("Your head hurts. ")
                    time.sleep(0.7)
                    print()
                    print("You feel hot. ")
                    time.sleep(0.9)
                    print()
                    print("Everything is spinning. It seems there was a goblin waiting for you to continue walking... ")
                    death(name, xp)


        elif forest_choice_one.strip().lower() == "leave":
            xp = xp + random.randint(1,20)
            print("You leave the forest, walking towards the graveyard...")
            graveyard(name, xp, forest_choices_made)

            forest_choices_made = True


def old_hotel(name, xp, forest_choices_made):
    forest_choices_made = True
    print("Old Hotel")

def bedroom():
    print("Bedroom.")

def nursery():
    print("Nursery.")

def graveyard(name, xp, forest_choices_made):
    forest_choices_made = True
    print("Graveyard.")

def death(name, xp):
    playsound('death.mp3', block=False)
    time.sleep(4)
    print(f"{name} died with {xp} experience points. ")
    sys.exit()

name = game_start(start_system_confirmed)


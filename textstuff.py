import random

def spawn(you, mon):
    print(f"~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
    print(f"{you} encountered a {mon}")
    print(f"~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")

def tired(mon):
    print(f"The {mon} is tired...")

def defeat(you, mon):
    print(f"% * * * * * * * * * * * * * * %")
    print(f"{you} defeated the {mon}!")
    print(f"% * * * * * * * * * * * * * * %\n")

def rest(mon):
    print(f"The {mon} rests this turn...!")

def ded(you):
    print(f"~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
    print(f"{you}'s HP has been reduced to 0!")
    print("YOU DIED")


def naming():
    while True:
        name = input("What is your name?\n>")
        chance = random.randrange(1, 4) #picks a number from 1-5
        name = name.capitalize()

    #because it'd be funny
        if chance == 3:     #if 5 = good name
            choice = input(f"{name} is a good name! But are you sure?\n(y/n)>")
            if choice == "y":
                print("Good choice!")
                break
            elif choice == "n":
                print("Aaaaw :(")
            else:
                print("Invalid input!")
        else:                #otherwise, bad name
            choice = input(f"{name} is a dumb name, are you sure?\n(y/n)>")
            if choice == "y":
                print("Well, alrighty then...")
                break
            elif choice == "n":
                print("Decide better!")
            else:
                print("Invalid input!")
        print(f"-------------------------------")
    print(f"-------------------------------")
    return name
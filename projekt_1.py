"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Tomáš Škuta
email: tomasskuta@seznam.cz
discord: smajlikskutik
"""

from texts import *
import pwinput

USERS = {
    "bob":"123",
    "ann":"pass123",
    "mike":"password123",
    "liz":"pass123"
}

def main():

    username = input("Username: ")

    if username in USERS and USERS:

        password = pwinput.pwinput(prompt="Password: ",mask="*")

        if USERS[username] == password :
            print("----------------------------------------------------------------")
            print("Welcome to the app, "+username+" We have 3 texts to be analyzed.")
            print("----------------------------------------------------------------")

            selection = None
            while selection not in range(1,4):
                selection = int(input("Enter a number of the text to be analyzed (1-3): "))
                if selection not in range (1,4):
                    print("Not in range! Try again.")
                  
            print(TEXTS[selection-1])
                    
        else:
            print("Wrong password")

    else:
        print("Unregistered user, terminating the program..")

if __name__ == "__main__":
    main()


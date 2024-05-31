"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Tomáš Škuta
email: tomasskuta@seznam.cz
discord: smajlikskutik
"""

from texts import *
from users import *
import pwinput

def main():

    username = input("Username: ")
    password = pwinput.pwinput(prompt="Password: ", mask="*")

    if username in users and users[username] == password:
        print("----------------------------------------------------------------")
        print("Welcome to the app, "+username+", we have " + str(len(TEXTS)) + " texts to be analyzed.")
        print("----------------------------------------------------------------")

        try:
            selection = int(input("Enter a number of the text to be analyzed (1-" + str(len(TEXTS)) + "): "))
            if selection not in range (1, len(TEXTS) + 1):
                print("Invalid selection, terminating the program..")
                return        
        except ValueError:
            print("Invalid input, terminating the program..")
            return
        
        selected_text = TEXTS[selection - 1]
        print(selected_text)
        words = selected_text.split()
        words_count = len(words)
        print(words_count)

        words_with_capitals = 0
        for word in words:
            if word[0].isupper():
                words_with_capitals += 1
        print(words_with_capitals)        
                    
    else:
        print("Unregistered user, terminating the program..")

if __name__ == "__main__":
    main()


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
    print("--------------------------------------------------")
    print("Please enter your username and password.")
    print("--------------------------------------------------")
    username = input("Username: ")
    password = pwinput.pwinput(prompt="Password: ", mask="*")

    if username in users and users[username] == password:
        print("--------------------------------------------------")
        print(f"Welcome to the app, {username}.") 
        print(f"We have {str(len(TEXTS))} texts to be analyzed.")
        print("--------------------------------------------------")

        try:
            selection = int(input(f"Enter a number of the text to be analyzed (1-{str(len(TEXTS))}): "))
            print("--------------------------------------------------")
            if selection not in range (1, len(TEXTS) + 1):
                print("Invalid selection, terminating the program..")
                return          
        except ValueError:
            print("Invalid input, terminating the program..")
            return
        
        selected_text = TEXTS[selection - 1]
        words_split = selected_text.split()
        words = [(word.strip(".,?!-%+/*()§\"")) for word in words_split]

        words_count = len(words)
        print(f"There are {words_count} words in the selected text.")

        words_titlecase = sum(1 for word in words if word[0].isupper() and word[0].isalpha())
        print(f"There are {words_titlecase} titlecase words.")

        words_uppercase = sum(1 for word in words if word.isupper() and word.isalpha())
        print(f"There are {words_uppercase} uppercase words.")

        words_lowercase = sum(1 for word in words if word.islower() and word.isalpha()) 
        print(f"There are {words_lowercase} lowercase words.")

        numerics = sum(1 for word in words if word.isnumeric())
        print(f"There are {numerics} numeric strings.")

        numerics_count = sum(int(word) for word in words if word.isnumeric())
        print(f"The sum of all the numbers is {numerics_count}.")

        words_max_lenght = max([len(word) for word in words])

        max_occurrence = max(sum(1 for word in words if len(word) == i) for i in range(1, words_max_lenght + 1))
        max_occurrence_graph = str((int((max_occurrence-11)/2)) * " ")

        if max_occurrence % 2 == 0:
            max_occurrence_graph2 = max_occurrence_graph + " "
        else:
            max_occurrence_graph2 = max_occurrence_graph
        
        print("--------------------------------------------------")
        print(f"LEN|{max_occurrence_graph}OCCURRENCES{max_occurrence_graph2}|NR.")
        print("--------------------------------------------------")

        for i in range(1, words_max_lenght + 1):
            stats = sum(1 for word in words if len(word) == i)
            stats_graph = str(stats * "*")   
            print(f"{i:<3}|{str(stats_graph):<{max_occurrence}}|{stats}")    

    else:
        print("Unregistered user, terminating the program...")

if __name__ == "__main__":
    main()


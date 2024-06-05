"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Tomáš Škuta
email: tomasskuta@seznam.cz
discord: smajlikskutik
"""
# using files in case we would use .exe file so we can analyze any other text, same for users - those should be hashed iif used this way
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
        print(f"We have {str(len(TEXTS))} texts to be analyzed.")   # using len of text if we have more/other texts in next usage, also in other cases below
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
        
        selected_text = TEXTS[selection - 1].replace("-", " ")  # not sure if we had to replace buff-to-white with buff to white, depends on user requirements 
        words_split = selected_text.split()
        words = [(word.strip(".,?!-%+/*()§\"")) for word in words_split]    # deleting those characters, as we dont need them and those could make some troubles while counting below

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

        words_max_lenght = max([len(word) for word in words])   # getting maximum lenght of word in the text for the range of for cycle to getting max occurrence of words lenght

        max_occurrence = max(sum(1 for word in words if len(word) == i) for i in range(1, words_max_lenght + 1))    # getting maximum occurrence for "graph" to show exact lenght of maximum occurence (header wise) and also other lenghts wise
        max_occurrence_graph = str((int((max_occurrence - 11)/2)) * " ")  # variable for lenght of the occurrence column in header

        # this is fix of the graph lenght when max_occurence is even number
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


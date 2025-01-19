import json
import random
import sys
import os
QSets = {}
filepath = 'qsets.json'

# Made into its own function so no need to copy-paste it
def logo():
    print("  ___ _         _    ___             _ ")
    print(" | __| |__ _ __| |_ / __|__ _ _ _ __| |")
    print(" | _|| / _` (_-< ' \\ (__/ _` | '_/ _` |")
    print(" |_| |_\\__,_/__/_||_\\___\\__,_|_| \\__,_|")
    print(" ")


def clear_console():
    if "win" in sys.platform:
        os.system('cls')
    else:
        os.system('clear')


# All Menus are in here, they are in a class for organization sake.
class Menu():
    def main_menu(self):
        clear_console()
        logo()
        print("[1] Add Questions")
        print("[2] Question Sets")
        print("[3] Start Flashcard")
        print("[0] Exit\n")

        listener = input("")
        if listener == "0":
            sys.exit(0)
        elif listener == "1":
            self.adding_menu()
        elif listener == "2":
            self.qsets_menu()
        elif listener == "3":
            self.flashcard_menu()
        else:
            self.main_menu()


    def adding_menu(self):
        clear_console()
        logo()
        print("[0] Go Back.\n")

        listener = input("Enter your question: ")
        if listener == "0":
            self.main_menu()
            return
        
        question = listener
        answer = input("Enter your answer: ")

        QSets.update({question: answer})
        data = json.dumps(QSets)
        with open('qsets.json', 'w') as file:
            file.write(data)

        self.main_menu()


    def qsets_menu(self):
        clear_console()
        logo()
        print("[0] Go back.\n")

        questions = list(QSets.keys())
        for i in range(len(questions)):
            print(f'{i + 1}. {questions[i]}')
            print(f'{i + 1}. {QSets[questions[i]]}\n')

        listener = input("")
        if listener in ["0", ""] or int(listener) >= len(questions) + 1:
            self.main_menu()
            return
        
        QSets.pop(questions[int(listener) - 1])
        data = json.dumps(QSets)
        with open(filepath, 'w') as file:
            file.write(data)

        self.qsets_menu()
        

    def flashcard_menu(self):
        clear_console()
        logo()
        print("[0] Go back.\n")
        questions = list(QSets.keys())

        rand_index = random.randint(0, (len(questions) - 1))
        print(questions[rand_index])

        listener = input()
        if listener == "0":
            self.main_menu()
            return
        
        print(QSets[questions[rand_index]])
        listener_2 = input()
        if listener_2 == "0":
            self.main_menu()
            return
        
        self.flashcard_menu()


# Load the Question Sets from qsets.json
with open(filepath, 'r') as file:
    QSets.update(json.load(file))

# Open the main menu
Menu().main_menu()

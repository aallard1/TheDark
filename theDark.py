import random
import os


class entity(): # Player and enemy objects derive from me
    def __init__(self, health, mana, stamina, gold, experience, level):
        self.health = health
        self.mana = mana
        self.stamina = stamina
        self.gold = gold
        self.experience = experience
        self.level = level

class gameEngine():
    def __init__(self):
        pass

class color():
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def main():
    intro()

def clear_console(): # Clears the terminal window
    os.system('clear')

def intro():
    counter = 0
    print(color.RED + "It's dark..." + color.END)
    userInput = input(color.BOLD + "What will you do?\n(Press enter to quit.) " + color.END)
    while userInput != '':
        print(color.RED + "It's dark..." + color.END)
        counter += 1
        userInput = input(color.BOLD + "What will you do?\n(Press enter to quit.) " + color.END)
        if counter >= 3:
            clear_console()
            print(color.RED + "You hear laughter coming from somewhere nearby.\n'What a pathetic insect.', a voice in the darkness says.\n'" + color.END + "Follow " + color.RED + "the sound of my voice, vermin.'" + color.END)
            choiceInput = input(color.BOLD + "What will you do?\n(Press enter to quit.) " + color.END)
            choiceInput = choiceInput.lower()
            while choiceInput != '':
                if choiceInput == 'follow':
                    clear_console()
                    print('')
                    print(color.RED + "You follow the strange voice, as it leads you through the formless void." + color.END)
                    print('')
                    print(color.RED + "You bump into the stanger, suddenly able to see them for the first time.\nTheir tall form is vague in the darkness, but you can see wicked looking claws and vastly engorged limbs." + color.END)
                    print('')
                    print(color.RED + "As you shuffle backwards, still looking up at the warped figure, they look down at you, chuckling.\n'Well, now, I guess this is as far as we go. Goodbye, vermin.'" + color.END)
                    choiceInput = input(color.BOLD + "What will you do? [1] Fight [2] Flee\n(Press enter to quit.) " + color.END)
                    if choiceInput == '':
                        clear_console()
                        quit()
                else:
                    print(color.RED + "That was the wrong choice..." + color.END)
                    print(color.RED + "Your screams echo in the vast darkness as you are torn to pieces." + color.END)
                    counter = 0
                    choiceInput = input(color.BOLD + "Press any key to play again.\n(Press enter to quit.) " + color.END)
                    if choiceInput == '':
                        clear_console()
                        quit()
                    else:
                        clear_console()
                        intro()
            if choiceInput == '':
                clear_console()
                quit()
    if userInput == '':
        clear_console()
        quit()


if __name__ == "__main__":
    main()


""" TODO
- Implement console clear screen "cls" done!
"""
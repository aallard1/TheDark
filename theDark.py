import random
import os

MAX_START_STAT = 20
MIN_START_STAT = 5

class entity(): # Player and enemy objects derive from me
    def __init__(self, health, mana, stamina, gold, experience, level):
        self.health = health
        self.mana = mana
        self.stamina = stamina
        self.gold = gold
        self.experience = experience
        self.level = level

    # make changeN functions
    # def changeHealth(self, n: int):
    #     self.health += n
    def getHealth(self):
        return self.health

    def setHealth(self, n: int):
        self.health = n
    
    def getMana(self):
        return self.mana
    
    def setMana(self, n: int):
        self.mana = n
    
    def getStamina(self):
        return self.stamina

    def setStamina(self, n: int):
        self.stamina = n
    
    def getGold(self):
        return self.gold

    def setGold(self, n: int):
        self.gold = n
    
    def getExperience(self):
        return self.experience

    def setExperience(self, n: int):
        self.experience = n

    def getLevel(self):
        return self.level

    def setLevel(self, n: int):
        self.level = n


class gameEngine():
    def __init__(self):
        # self.exist = exist
        pass
            
    def start(self): # Start engine (main game functionality)
        counter = 0
        player = entity(20, random.randint(MIN_START_STAT, MAX_START_STAT), random.randint(MIN_START_STAT, MAX_START_STAT),0,0,1)
        enemy = entity(20, 10, 10, 0, 0, 1)
        whatDo = "What will you do?\n(Press 'q' to quit) "

        print(color.RED + "It's dark..." + color.END)
        userInput = input(color.BOLD + whatDo + color.END)
        userInput = userInput.lower()

        while userInput != 'q':
            if userInput == 'help' or userInput == 'h': # Reset condition
                print(color.RED + "No one can help you now." + color.END)
                quit()
            print(color.RED + "It's dark..." + color.END)
            counter += 1
            userInput = input(color.BOLD + whatDo + color.END)
            if counter >= 2:
                clear_console()
                print(color.RED + "You hear laughter coming from somewhere nearby.\n'What a pathetic insect.', a voice in the darkness says.\n'" + color.END + "Follow " + color.RED + "the sound of my voice, vermin.'" + color.END)
                userInput = input(color.BOLD + whatDo + color.END)
                userInput = userInput.lower()
                if userInput == 'follow' or userInput == 'f':
                    clear_console()
                    print(color.RED + "You follow the strange voice, as it leads you through the formless void." + color.END + "\n")
                    print(color.RED + "You bump into the stanger, suddenly able to see them for the first time.\nTheir tall form is vague in the darkness, but you can see wicked looking claws and vastly engorged limbs." + color.END + "\n")
                    print(color.RED + "As you shuffle backwards, still looking up at the warped figure, they look down at you, chuckling.\n'Well, now, I guess this is as far as we go. Goodbye, vermin.'" + color.END)
                    userInput = input(color.BOLD + "What will you do? [1] Fight [2] Flee\n(Press 'q' to quit.) " + color.END)
                    if userInput == '1':
                        clear_console()
                        print(color.RED + "You have chosen to fight for your life..." + color.END)
                        self.combat(player, enemy) # DOesn't do anything
                    elif userInput == '2':
                        print(color.RED + "You attempt to flee..." + color.END)
                        if player.stamina > 10:
                            print(color.RED + "You manage to flee from combat." + color.END)
                            userInput = input(color.BOLD + whatDo + color.END)
                        else:
                            print(color.RED + "You fail to flee from combat." + color.END)
                            userInput = input(color.BOLD + "What will you do? [1] Fight [2] Flee\n(Press 'q' to quit.) " + color.END)
                else:
                    print(color.RED + "That was the wrong choice..." + color.END)
                    print(color.RED + "Your screams echo in the vast darkness as you are torn to pieces." + color.END)
                    counter = 0
                    userInput = input(color.BOLD + "Press any key to play again.\n(Press 'q' to quit.) " + color.END)
                    if userInput != '':
                        clear_console()
                        self.start()                       
        if userInput == 'q':
            clear_console()
            quit()
    
    def combat(self, player, enemy):
        fightInput = ""
    
        while fightInput != 'q':
            clear_console()
            print(color.BOLD + "Player Stats     Enemy Stats\nHP: " + color.END + str(player.getHealth()) + color.BOLD + " MP: " + color.END + str(player.getMana()) + color.BOLD + "    HP: " + color.END + str(enemy.getHealth()) + color.BOLD + " MP: " + color.END + str(enemy.getMana()))
            fightInput = input(color.BOLD + "What will you do? [1] Attack [2] Defend [3] Flee\n(Press 'q' to quit.) "+ color.END)
            fightInput = fightInput.lower()
            if fightInput == '1':
                print("You hit them")
                pass
            elif fightInput == '2':
                print("Preparing for an onslaught")
                pass
            elif fightInput == '3':
                print(color.RED + "You attempt to flee..." + color.END)
                if player.stamina > 10:
                    print(color.RED + "You manage to flee from combat." + color.END)
                else:
                    print(color.RED + "You fail to flee from combat." + color.END)
                    fightInput = input(color.BOLD + "What will you do? [1] Attack [2] Defend [3] Flee\n(Press 'q' to quit.) "+ color.END)
            else:
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
    game = gameEngine()
    game.start()

def clear_console(): # Clears the terminal window
    os.system('clear')

if __name__ == "__main__":
    main()

""" TODO
- Implement console clear screen "cls" done!
- Unfriendly UX, always let user know how to play
- HP: ? | MP: ?
"""
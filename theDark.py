import random

def main():
    intro()

def intro():
    counter = 0
    print("It's dark...")
    userInput = input("What will you do? (Press enter to quit) ")
    while userInput != '':
        print("It's dark...")
        counter += 1
        userInput = input("What will you do?\n(Press enter to quit) ")
        if counter >= 4:
            print("You hear laughter coming from somewhere nearby.\n'What a pathetic insect.', a voice in the darkness says.\n'Follow the sound of my voice, vermin.'")
            choiceInput = input("What will you do?\n(Press enter to quit) ")
            choiceInput = choiceInput.lower()
            while choiceInput != '':
                if choiceInput == 'follow':
                    pass
                else:
                    print("That was the wrong choice...")
                    print("Your screams echo in the vast darkness as you are torn to pieces.")
                    counter = 0
                    choiceInput = input("Press any key to play again.\n(Press enter to quit) ")
                    if choiceInput == '':
                        quit()
                    while choiceInput != '':
                        break
    if userInput == '':
        quit()


if __name__ == "__main__":
    main()
import random
TheNumber = random.randint(0, 10)
# Number Guessing Game

# Concepts: Input handling, conditionals, random module.
# Description: Create a game where the program randomly selects a number within a range, and the player has to guess it.
#  You can give hints like “too high” or “too low” until they guess correctly.

def GuessingABloodyNumber():
    global TheNumber
    print("A Number from 0 to 10 = You Guess, if guess != correct: os.remove(system32).")
    print("Starting.")
    print("Generating a Number....")
    print("Beeep.")
    print("Booop.")
    print("You Number has been Generated, Now tell me what is it. ")
    while True:
        userGuess = int(input(": "))
        if userGuess > TheNumber:
            print("Too Bigh Number. ")
        elif userGuess < TheNumber:
            print("Too Smallh Number. ")
        elif userGuess == TheNumber:
            print(f"You Won, Your Guesss {userGuess} is equal to the original number {TheNumber}.")
            break
        else:
            print("Tf you doing? I said a number")


GuessingABloodyNumber()
from guessNumberArt import logo
from random import randint
def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "hard":
        attempts = 5
    elif difficulty == "easy":
        attempts = 10
    theAnswer = randint(1,100)
    while(attempts):
        print(f"You have {attempts} attempts remaining to guess the number.")
        userGuess = int(input("Make a guess: "))
        if(userGuess == theAnswer):
            print(f"Correct Answer, the answer was {theAnswer} winner 🎊🎉🎈")
            break
        else:
            attempts -= 1
            if userGuess < theAnswer:
                print("Too low.")
            else:
                print("Too high.")
            if attempts > 1: print("Guess again.")
            else: print("You've run out of guesses, you lose.")
play_game()

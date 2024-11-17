from random import randint
from art import logod,logoe,logof
print(logod)
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess,answer,turns):
    """Checks ans and return the number of turns remaining"""
    if guess>answer:
        print("Too high")
        return turns - 1
    elif guess<answer:
        print("Too Low")
        return turns - 1
    else:
        print(logoe)
        print(f"Yayyy.... YOU GOT !! CORRECT ANSWER {answer}.")
#Make function to set difficulty
def set_difficulty():
    difficulty = input("Choose difficulty.Type 'easy' or 'hard' : ")
    if difficulty == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    #Choosing the random number between 1 and 100.
    print("Welcome to the number Guessing game")
    print("Im thinking of a number between 1 and 100")
    answer = randint(1, 100)
    #print(f"The correct answer is {answer}")
    #------------------------------------------------------------
    turns = set_difficulty()

    #User guess the number
    guess = 0
    while guess!= answer:
        print(f"You have {turns} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        turns= check_answer(guess, answer,turns)
        if turns == 0:
            print(logof)
            print("You have run out of guesses and You lost the game")
            return
        elif guess!=answer:
            print("Guess Again. !!")

    #Track the number of turnes and make it -1 for every turn
game()
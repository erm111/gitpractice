import random

# generate a random number between 1 and 10
number = random.randint(1, 10)

# prompt the user to guess the number
print("I'm thinking of a number between 1 and 10. Can you guess what it is?")
guess = int(input())

# keep track of the number of guesses
num_guesses = 1

# loop until the user guesses the number correctly
while guess != number:
    # give the user a hint
    if guess < number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")
        
    # get another guess from the user
    guess = int(input())
    num_guesses += 1

# congratulate the user and tell them how many guesses it took
print("Congratulations, you guessed the number! It took you", num_guesses, "guesses.")

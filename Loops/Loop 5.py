import random
print("Welcome to the Magical Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("But beware, the number might change its mind!")
secret_number = random.randint(1, 100)


while True:
    for guess_count in range(1, 6):  # 5 guesses before the number changes
        print(guess_count)
  # Your code here: Ask for a guess
        guess = int(input("Guess a number between 1 and 100 "))
    # Your code here: Check if the guess is correct, if it is, tell the user they won and break out of the for loop
        if int(guess) == secret_number:
            print("you did it!")
            break

    # Your code here: If the guess is incorrect, give hints (too high/too low)

        elif int(guess) > secret_number:
            print("incorrect too high")
        else:
            print("incorrect too low")

# Your code here: Ask if the player wants to continue.

    try_again= input("do you want to play again? y/n")
    if try_again == "y":
        secret_number = random.randint(1, 100)

    else:
        break

# If they want to continue, change the secret number to a new random number.
# Ifthey do not want to continue, break out of the while loop.

# Your code here: Display the secret number and thank the user for playing.
print("The secret number is ")
print(secret_number)
print("Thanks for playing!")


# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input("Guess: "))
#     guess_count += 1
#     if guess == secret_number:
#         print("You won! ")
#         break
# else:
#     print("You Lose! ")


# 	1.	Chooses a secret number between 1 and 20.
# 	2.	Allows the user to guess the number, giving them up to 5 attempts.
# 	3.	After each guess, tell the user if their guess is too high, too low, or correct.
# 	4.	If the user guesses correctly, print "Congratulations! You guessed the number!".
# 	5.	If they run out of attempts, print "Sorry, you've run out of guesses. The number was X." where X is the secret number.

# secret_number = int(input("enter the number: "))
# guess_count = 0
# guess_limit = 5
# while guess_count < guess_limit:
#     guess = int(input("guess: "))
#     guess_count += 1
#     if guess == secret_number:
#         print("Congratulations! you guessed the number! ")
#         break
# else:
#     print("Sorry, you've run out of guesses.")

import random

# 1. Choose a secret number between 1 and 20
secret_number = random.randint(1, 20)
guess_count = 0
guess_limit = 5

print("I'm thinking of a number between 1 and 20. You have 5 attempts to guess it.")

# 2. Allow the user to guess the number with up to 5 attempts
while guess_count < guess_limit:
    try:
        guess = int(input("Enter your guess: "))
        guess_count += 1

        # 3. Give feedback on each guess
        if guess == secret_number:
            print("Congratulations! You guessed the number!")
            break
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")

    except ValueError:
        print("Please enter a valid number.")

# 5. If they run out of attempts, show the correct number
if guess_count == guess_limit and guess != secret_number:
    print(f"Sorry, you've run out of guesses. The number was {secret_number}.")
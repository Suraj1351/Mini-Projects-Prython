import random

print("Welcome to the Number guesser Game!")

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(0,5)

while True:
    user_guess = input("Make a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Sorry, that's not a number. Try again.")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    else:
        print("You got it wrong! Try again.")

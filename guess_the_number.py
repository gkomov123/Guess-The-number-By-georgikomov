import random

number_to_guess = random.randint(1, 100)

guesses = 0

while True:
    number = int(input("Guess a number: "))
    guesses += 1

    if number > number_to_guess:
        print("Too high")
    elif number < number_to_guess:
         print("Too low")
    elif number == number_to_guess:
        print("You Win!")
        print(f"Guesses: {guesses}")
        break




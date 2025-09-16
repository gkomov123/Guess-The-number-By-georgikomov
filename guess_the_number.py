import random

number_to_guess = random.randint(1, 100) # Chooses a random number from 1 to 100
difficulty = input("Choose a diffuculty (e), (m), (h): ") # asks the player for a  difficulty 

guesses = 0

# Difficulty logic
if difficulty == "e":
    max_guesses = 15
elif difficulty == "m":
    max_guesses = 10
elif difficulty == "h":
    max_guesses = 5
else:
    max_guesses = 10

while guesses < max_guesses:
    number = int(input("Guess a number: "))
    guesses += 1

    if number > number_to_guess:
        print("Too high")
    elif number < number_to_guess:
         print("Too low")
    elif number == number_to_guess:
        print("-------------")
        print("You Win!")
        print(f"Guesses: {guesses}")
        print(f"The number was: {number_to_guess}")
        break
else:
    print("-----------------")
    print("Out of guesses")
    print(f"The number was: {number_to_guess}")
    print("-----------------")



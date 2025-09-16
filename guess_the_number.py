import random

while True: #Main loop which checks if the player wants to play

     # Chooses a random number from 1 to 100
    number_to_guess = random.randint(1, range_max)

    difficulty = input("Choose a diffuculty (e), (m), (h): ") # asks the player for a  difficulty 

# Difficulty logic
    if difficulty == "e":
        range_max = 100
        max_guesses = 15
    elif difficulty == "m": 
        range_max = 200
        max_guesses = 10
    elif difficulty == "h":
        range_max = 300
        max_guesses = 5
    else:
        range_max = 200
        max_guesses = 10
    
    guesses = 0

    # Loop for the game logic
    while guesses < max_guesses:
        number = int(input("Guess a number: "))
        guesses += 1

        if number > number_to_guess:
            print("Too high")
        elif number < number_to_guess:
            print("Too low")
        else:
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
        
    
    play_again = input("Do you want to keep playin? (y), (n): ")
    if play_again != "y":
        print("Thanks for playing!")
        break



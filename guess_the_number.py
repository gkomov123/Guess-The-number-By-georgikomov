import random
import time

while True: #Main loop which checks if the player wants to play
    
    difficulty = input("Choose a diffuculty (e), (m), (h), (c), (i), (t): ").lower() # asks the player for a  difficulty 

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
    elif difficulty == "c":
        range_max = int(input("Enter the maximum number: "))
        max_guesses = int(input("Enter how many guesses you want: "))
    elif difficulty == "i":
        range_max = 1000
        max_guesses = 1
    elif difficulty == "t":
        range_max = 100
        max_guesses = float("inf")
        time_limit = 30 #SECONDS
        start_time = time.time()
        
    else:
        range_max = 200
        max_guesses = 10

    # Chooses a random number from 1 to 100
    number_to_guess = random.randint(1, range_max)    
    
    guesses = 0


    # Loop for the game logic
    while guesses < max_guesses:

        if difficulty == "t" and (time.time() - start_time) > time_limit:
            print("⏰ Time's up! You lose.")
            break

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
            print(f"It took you, {int(time.time() - start_time)}s, to guess the number")
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



import random
import time
import sys
import threading

def start_timer(time_limit):
    def timer_end():
        time.sleep(time_limit)
        print("\n⏰ Time's up! You lose.")
        sys.exit() #force quit the game
    t = threading.Thread(target=timer_end, daemon=True)
    t.start


while True: #Main loop which checks if the player wants to play

    # asks the player for a  difficulty 
    difficulty = input("Choose a difficulty (e = easy, m = medium, h = hard, i = insane, " \
                        "c = custom, t = time attack): ").lower() 
    

# Difficulty logic
    if difficulty == "e":
        range_max = 100
        max_guesses = 15
        time_limit = None
    elif difficulty == "m": 
        range_max = 200
        max_guesses = 10
        time_limit = None
    elif difficulty == "h":
        range_max = 300
        max_guesses = 5
        time_limit = None
    elif difficulty == "c":
        range_max = int(input("Enter the maximum number: "))
        max_guesses = int(input("Enter how many guesses you want: "))
        time_limit = None
    elif difficulty == "i":
        range_max = 1000
        max_guesses = 1
        time_limit = None
    elif difficulty == "t":
        range_max = 100
        max_guesses = float("inf")
        time_limit = int(input("Time limit (seconds): ")) #SECONDS
        start_timer(time_limit)
    else:
        range_max = 200
        max_guesses = 10
        time_limit = None

    # Chooses a random number from 1 to 100
    number_to_guess = random.randint(1, range_max)    
    
    # guesses counter and round start timer
    guesses = 0
    round_start = time.time()

    # Loop for the game logic
    while guesses < max_guesses:

        # Guess Input and guess incrementer    
        number = int(input("Guess a number: "))
        guesses += 1

        if number > number_to_guess:
            print("Too high") # if the number guessed is higher than the number to guess
        elif number < number_to_guess: # if the number guessed is lower than the number to guess
            print("Too low")
        else: # Win prints
            print("-------------")
            print("You Win!")
            print(f"Guesses: {guesses}")
            print(f"The number was: {number_to_guess}")
            elapsed = time.time() - round_start
            print(f"It took you, {elapsed:.2f}s, to guess the number")
            break
    else: # Ran out of guesses case
        if difficulty != "t":
            print("-----------------")
            print("Out of guesses")
            print(f"The number was: {number_to_guess}")
            print("-----------------")
        
    # Play again logic
    play_again = input("Do you want to keep playin? (y), (n): ")
    if play_again != "y":
        print("Thanks for playing!")
        break



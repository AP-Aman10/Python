# Snake, Water & Gun game with rounds, points, and ANSI colors
import random

# ANSI color codes
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
RESET = "\033[0m"

options = ["Snake", "Water", "Gun"]

# Function to determine winner
def determine_winner(player, computer):
    if player == computer:
        return "Tie"
    elif (player == "Snake" and computer == "Water") or \
         (player == "Water" and computer == "Gun") or \
         (player == "Gun" and computer == "Snake"):
        return "Player"
    else:
        return "Computer"

# Initialize scores and rounds
player_score = 0
computer_score = 0
round_number = 1

print(f"{CYAN}Welcome to the Snake, Water & Gun Game!{RESET}")

while True:
    print(f"\n{YELLOW}--- Round {round_number} ---{RESET}")
    print(f"{YELLOW}Options: Snake, Water, Gun{RESET}")
    
    player_choice = input(f"{RED}Enter your choice (or 'quit' to exit): {RESET}").capitalize()
    if player_choice == "Quit":
        print(f"{MAGENTA}\nThanks for playing! Final Scores:{RESET}")
        print(f"{GREEN}Player: {player_score}{RESET} | {RED}Computer: {computer_score}{RESET}")
        break
    if player_choice not in options:
        print(f"{RED}Invalid choice! Please try again.{RESET}")
        continue
    
    computer_choice = random.choice(options)
    print(f"{BLUE}Computer chose: {computer_choice}{RESET}")
    
    winner = determine_winner(player_choice, computer_choice)
    
    if winner == "Tie":
        print(f"{MAGENTA}It's a tie!{RESET}")
    elif winner == "Player":
        print(f"{GREEN}You won this round!{RESET}")
        player_score += 1
    else:
        print(f"{RED}Computer won this round!{RESET}")
        computer_score += 1
    
    print(f"{CYAN}Score -> Player: {player_score} | Computer: {computer_score}{RESET}")
    round_number += 1

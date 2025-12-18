import random
import time

# Color codes
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
RESET = "\033[0m"

def main():
    random_number = random.randint(1, 1000+1)
    no_of_guesses = 0

    print(f"{CYAN}🎯 Welcome to the Number Guessing Game!{RESET}")
    print(f"{YELLOW}I'm thinking of a number between 1 and 1000...{RESET}\n")
    print(f"{random_number}")

    while True:
        try:
            guessed_number = int(input(f"{BLUE}👉 Guess the number: {RESET}"))
        except ValueError:
            print(f"{RED}❌ Please enter a valid number!{RESET}\n")
            continue

        no_of_guesses += 1

        if guessed_number > random_number:
            print(f"{MAGENTA}⬇️  Guess Lower number please!{RESET}\n")
        elif guessed_number < random_number:
            print(f"{MAGENTA}⬆️  Guess Higher number please!{RESET}\n")
        else:
            # Player guessed correctly
            print(f"{GREEN}🎉 Congrats!! You guessed the number!{RESET}\n")

            if no_of_guesses == 1:
                print(f"{YELLOW}💥 Incredible! You guessed it on your FIRST try!!{RESET}")
            elif no_of_guesses <= 3:
                print(f"{CYAN}🔥 Amazing! You’re a natural guesser!{RESET}")
            elif no_of_guesses <= 7:
                print(f"{BLUE}👍 Well done! That was pretty good!{RESET}")
            else:
                print(f"{WHITE}😅 You got it! Took a few tries, but that’s okay!{RESET}")
            break

        time.sleep(0.5)

    print(f"\n{GREEN}✅ You guessed the number in {RED}{no_of_guesses}{GREEN} guesses.{RESET}")

if __name__ == "__main__":
    main()
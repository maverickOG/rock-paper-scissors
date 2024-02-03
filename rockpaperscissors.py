import random

def play_again():
    """Asks the user if they want to play again.

    Returns:
        bool: True if the user wants to play again, False otherwise.
    """
    while True:
        answer = input("Do you want to play again? (y/n): ").lower()
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def main():
    """Runs the rock, paper, scissors game with scorekeeping."""

    print("Welcome to Rock, Paper, Scissors!")

    user_score = 0
    computer_score = 0

    while True:
        options = ["rock", "paper", "scissors"]
        user_choice = input("Choose rock, paper, or scissors: ").lower()

        if user_choice not in options:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
            continue

        computer_choice = random.choice(options)

        print(f"\nYou chose {user_choice}, computer chose {computer_choice}.")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif user_choice == "rock":
            if computer_choice == "scissors":
                print("You win! Rock smashes scissors.")
                user_score += 1
            else:
                print("You lose! Paper covers rock.")
                computer_score += 1
        elif user_choice == "paper":
            if computer_choice == "rock":
                print("You win! Paper covers rock.")
                user_score += 1
            else:
                print("You lose! Scissors cuts paper.")
                computer_score += 1
        elif user_choice == "scissors":
            if computer_choice == "paper":
                print("You win! Scissors cuts paper.")
                user_score += 1
            else:
                print("You lose! Rock smashes scissors.")
                computer_score += 1

        print(f"\nCurrent score: User - {user_score}, Computer - {computer_score}")

        if not play_again():
            # Display final score when user chooses not to play again
            print(f"\nFinal score: User - {user_score}, Computer - {computer_score}")
            break

if __name__ == "__main__":
    main()

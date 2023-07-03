import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "scissors" and computer_choice == "paper")
        or (user_choice == "paper" and computer_choice == "rock")
    ):
        return "user"
    else:
        return "computer"

def print_score(user_wins, computer_wins, draws):
    print("Score:")
    print(f"User: {user_wins}   Computer: {computer_wins}   Draws: {draws}")

def play_game():
    choices = ["rock", "paper", "scissors"]
    user_wins = 0
    computer_wins = 0
    draws = 0

    print("Welcome to Rock, Paper, Scissors!")
    print("Enter 'q' to quit.")

    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

        if user_choice == "q":
            break

        if user_choice not in choices:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer's choice: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)

        if winner == "user":
            user_wins += 1
            print("You win!")
        elif winner == "computer":
            computer_wins += 1
            print("Computer wins!")
        else:
            draws += 1
            print("It's a draw!")

        print_score(user_wins, computer_wins, draws)
        print()

    print("Thanks for playing!")

play_game()

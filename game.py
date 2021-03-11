import random

while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"You both selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock beats scissors! You win!")
        else:
            print("Paper beats rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper beats rock! You win!")
        else:
            print("Scissors beats paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors beats paper! You win!")
        else:
            print("Rock beats scissors! You lose.")

    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != "y":
        break
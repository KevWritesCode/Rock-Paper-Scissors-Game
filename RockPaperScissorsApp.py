import random

print("Rock, Paper, Scissors")

# Keep track of player and CPU wins
player_wins = 0
cpu_wins = 0

while True:
    # The options the player can choose from
    options = ["rock", "paper", "scissors"]

    # The player's choice
    player_choice = input("Enter your choice (rock/paper/scissors) or type 'exit' to quit: ").lower()
    
    # Check if the player wants to exit
    if player_choice == "exit":
        break

    # Check if the player's choice is valid
    if player_choice not in options:
        print("Invalid choice! Please enter rock, paper, or scissors.")
        continue

    # The computer's choice
    computer_choice = random.choice(options)

    print("You chose", player_choice)
    print("The computer chose", computer_choice)

    # Determine the winner
    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == "rock" and computer_choice == "scissors":
        print("You win!")
        player_wins += 1
    elif player_choice == "paper" and computer_choice == "rock":
        print("You win!")
        player_wins += 1
    elif player_choice == "scissors" and computer_choice == "paper":
        print("You win!")
        player_wins += 1
    else:
        print("The computer wins!")
        cpu_wins += 1
    
    # Ask the player if they want to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "no":
        break

print("Player wins:", player_wins)
print("CPU wins:", cpu_wins)

import random


def get_player_choice():
    while True:
        choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")


def Computer_Choice():
    return random.choice(['rock', 'paper', 'scissors'])


def Who_wins(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
            (player_choice == 'paper' and computer_choice == 'rock') or \
            (player_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"


def play_game():
    player_wins = 0
    computer_wins = 0

    while player_wins < 2 and computer_wins < 2:
        print("\nRound {}:".format(player_wins + computer_wins + 1))
        player_choice = get_player_choice()
        computer_choice = Computer_Choice()
        print("Computer chooses", computer_choice)

        result = Who_wins(player_choice, computer_choice)
        print(result)

        if result == "You win!":
            player_wins += 1
        elif result == "Computer wins!":
            computer_wins += 1

    if player_wins > computer_wins:
        print("\nYou win the game!")
    else:
        print("\nComputer wins the game!")


def main():
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()

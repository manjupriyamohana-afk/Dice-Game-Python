# dice_game.py

import random

# Roll dice
def roll_dice():
    return random.randint(1, 6)

# Play one round
def play_round():
    input("\nPress Enter to roll the dice...")

    player_roll = roll_dice()
    computer_roll = roll_dice()

    print("You rolled:", player_roll)
    print("Computer rolled:", computer_roll)

    if player_roll > computer_roll:
        print("You win this round!")
        return "player"
    elif player_roll < computer_roll:
        print("Computer wins this round!")
        return "computer"
    else:
        print("It's a tie!")
        return "tie"

# Main game
def play_game():
    print("Welcome to Dice Game (Player vs Computer)")

    player_score = 0
    computer_score = 0
    rounds = 5

    for i in range(1, rounds + 1):
        print("\n--- Round", i, "---")
        result = play_round()

        if result == "player":
            player_score += 1
        elif result == "computer":
            computer_score += 1

        print("Score -> You:", player_score, "| Computer:", computer_score)

    print("\nGame Over!")
    print("Final Score -> You:", player_score, "| Computer:", computer_score)

    if player_score > computer_score:
        print("Congratulations! You won the game!")
    elif player_score < computer_score:
        print("Computer wins the game!")
    else:
        print("The game is a draw!")

# Run game
play_game()

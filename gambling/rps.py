from main.player import player
import random

def bid(amount):
    if amount > player.money:
        print("You don't have enough money to bid that amount.")
        return False
    else:
        player.money -= amount
        print(f"You bid ${amount}.")
        return True

def rock_paper_scissors(bid_amount):
    if bid(bid_amount):
        choices = ["rock", "paper", "scissors"]
        player_choice = input("Choose rock, paper, or scissors: ").lower()
        if player_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            return
        computer_choice = random.choice(choices)
        print(f"The computer chose {computer_choice}.")
        
        if player_choice == computer_choice:
            print("It's a tie!")
            player.money += bid_amount  # Refund the bid amount
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
            player.money += bid_amount * 2  # Add the winnings
        else:
            print("You lose.")
            # No need to do anything here, as the bid amount is already deducted.
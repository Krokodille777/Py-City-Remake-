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


#Guess a number between 1 and 10
def guess_number(bid_amount):
    if bid(bid_amount):
        tries = 3
        print(f"You have {tries} tries to guess the number between 1 and 10.")
        target = random.randint(1, 10)
        while tries > 0:
            guess = int(input("Guess a number between 1 and 10: "))

            if guess == target:
                winnings = bid_amount * 2
                player.money += winnings
                print(f"Congratulations! You guessed the number {target}. You won ${winnings}!")
                return
            else:
                tries -= 1
                print(f"Wrong guess. You have {tries} tries left.")

        print(f"Game over. The number was {target}.")
        player.money -= bid_amount
        print("You lost the bid.")
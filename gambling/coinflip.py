from main.player import player
import random
def bid(amount):
    if amount > player.money:
        print("You don't have enough money to bid that amount.")
        return False
    else:
        player.money -= amount
        print (f"You bid ${amount}.")
        return True


def coinflip(bid_amount):
    if bid(bid_amount):
        flip = random.choice(["heads", "tails"])
        print(f"The coin landed on {flip}.")
        if flip == "heads":
            winnings = bid_amount * 2
            player.money += winnings
            print(f"You won ${winnings}!")
        else:
            player.money -= bid_amount
            print("You lost the bid.")

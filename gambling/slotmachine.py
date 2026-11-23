from main.player import player
import random

# Slot machine has 3 reels and 3 symbols: cherry, lemon, and orange. The player can bet an amount of money and pull the lever. If all 3 symbols match, the player wins 10 times their bet. If 2 symbols match, the player wins 2 times their bet. If no symbols match, the player loses their bet.
def bid(amount):
    if amount > player.money:
        print("You don't have enough money to bid that amount.")
        return False
    else:
        player.money -= amount
        print(f"You bid ${amount}.")
        return True

def pull_lever(bid_amount):
    if bid(bid_amount):
        symbols = ["cherry", "lemon", "orange"]
        reel1 = random.choice(symbols)
        reel2 = random.choice(symbols)
        reel3 = random.choice(symbols)
        print(f"The reels show: {reel1}, {reel2}, {reel3}.")
        
        if reel1 == reel2 == reel3:
            winnings = bid_amount * 10
            player.money += winnings
            print(f"You won ${winnings}!")
        elif reel1 == reel2 or reel1 == reel3 or reel2 == reel3:
            winnings = bid_amount * 2
            player.money += winnings
            print(f"You won ${winnings}!")
        else:
            print("You lost the bid.")
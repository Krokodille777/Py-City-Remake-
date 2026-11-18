from items.catalog import available
from main.player import player
from money.balance import show_balance
import random

# When the gift box is opened, a random item from the available items in the shop will be added to the player's inventory
# There's a chance (25%) gift box will give money
# There is a rare chance that the gift box is empty and gives nothing. The chance of this happening is 5%.
def get_random_item():
    random_item_name = random.choice(list(available.keys()))
    print(f"You opened the gift box and received a {random_item_name}!")
    return random_item_name

def get_random_money():
    random_money = random.randint(50, 500)  # Random amount of money between 50 and 500
    print(f"You opened the gift box and received ${random_money}!")
    return random_money

def get_nothing():
    print("You opened the gift box, but it was empty. Better luck next time!")
    player.set_happiness(max(0, player.get_happiness() - 5))  # Decrease happiness by 5 points
    player.set_luck(max(0, player.get_luck() - 1))  # Decrease luck by 1 point
    return None

def open_gift_box():
    if player.inventory.get("gift_box", 0) <= 0:
        print("You don't have any gift boxes to open.")
        return



    player.inventory["gift_box"] -= 1
    if player.inventory["gift_box"] == 0:
        del player.inventory["gift_box"]

    # Randomly decide whether to give an item or money (50% chance for each)
    if random.choice([True, False]):
        item_name = get_random_item()
        player.inventory[item_name] = player.inventory.get(item_name, 0) + 1
        if item_name in ["house", "car", "diamond", "emerald", "ruby", "pizza", "cake", "energy_drink", "beer"]:
            player.set_happiness(min(100, player.get_happiness() + 10))  # Increase happiness by 10 points for receiving a rare item
            print(f"Your happiness has increased by 10 points for receiving a {item_name}.")
            player.set_luck(min(10, player.get_luck() + 0.5))  # Increase luck by 0.5 points for receiving a rare item
    elif random.random() < 0.05:  # 5% chance to get nothing
        get_nothing()
    else:
        money_amount = get_random_money()
        player.set_money(player.get_money() + money_amount)
        if money_amount >= 300:
            player.set_happiness(min(100, player.get_happiness() + 10))
            print("You received a high amount of money, so your happiness has increased by 10 points.")
            player.set_luck(min(10, player.get_luck() + 1))  # Increase luck by 1 point for receiving a high amount of money

        show_balance()  # Show the updated balance after receiving money


        

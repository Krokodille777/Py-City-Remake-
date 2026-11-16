from items.catalog import available
from main.player import player
from money.balance import show_balance

def buy_item(item_name, quantity):
    if quantity <= 0:
        print("Invalid quantity. Please enter a positive integer.")
        return
    price = available.get(item_name)
    if price is None:
        print(f"Item '{item_name}' is not available in the shop.")
        return
    total_cost = price * quantity
    if item_name in available:
        if player.get_money() >= total_cost:
            player.set_money(player.get_money() - total_cost)
            player.inventory[item_name] = player.inventory.get(item_name, 0) + quantity
            print(f"Bought {quantity} {item_name}(s) for ${total_cost}.")
        else:
            print("Not enough money to buy this item.")
    else:
        print("Item not available in the shop.")
    show_balance()

def sell_item(item_name, quantity):
    price = available.get(item_name)
    if quantity <= 0:
        print("Invalid quantity. Please enter a positive integer.")
        return
    if price is None:
        print(f"Item '{item_name}' is not available in the shop.")
        return
    if item_name in player.inventory and player.inventory[item_name] >= quantity:
        total_earnings = price * quantity /2
        player.set_money(player.get_money() + total_earnings)
        player.inventory[item_name] -= quantity
        if player.inventory[item_name] == 0:
            del player.inventory[item_name]
        print(f"Sold {quantity} {item_name}(s) for ${total_earnings}.")
    else:
        print("Not enough items to sell.")
    show_balance()

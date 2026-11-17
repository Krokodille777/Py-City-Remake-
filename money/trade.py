from items.catalog import available
from main.player import player
from money.balance import show_balance
from items.use.eat import update_expired
import time


def buy_item(item_name, quantity):
    item = available.get(item_name)
    if item is None:
        print(f"Item '{item_name}' is not available in the shop.")
        return
    if quantity <= 0:
        print("Invalid quantity. Please enter a positive integer.")
        return
    price = item["price"]
    total_cost = price * quantity
    if player.get_money() < total_cost:
        print("Not enough money to buy this item.")
        show_balance()
        return

    player.set_money(player.get_money() - total_cost)
    player.inventory[item_name] = player.inventory.get(item_name, 0) + quantity
    print(f"Bought {quantity} {item_name}(s) for ${total_cost}.")

    if item_name in ["house", "car"]:
        player.set_happiness(min(100, player.get_happiness() + item["happiness"]))
        print(f"Your happiness has increased by {item['happiness']} points for buying a {item_name}.")
    if item["type"] in ["food", "drink"]:
        player.bought_at.setdefault(item_name, []).extend([time.time()] * quantity)
    show_balance()

def sell_item(item_name, quantity):
    is_expired = item_name.startswith("expired")
    item = available.get(item_name.removeprefix("expired "))
    if item is None:
        print(f"Unknown item '{item_name}'.")
        return
    price = item["price"]
    if quantity <= 0:
        print("Invalid quantity. Please enter a positive integer.")
        return
    if player.inventory.get(item_name, 0) < quantity:
        print("Not enough items to sell.")
        show_balance()
        return

    if is_expired:
        total_earnings = price * quantity // 4  # expired items sell for a quarter of the price
    else:
        total_earnings = price * quantity // 2  # fresh items sell for half of the price
        times = player.bought_at.get(item_name, [])
        del times[:quantity]  # forget the oldest purchase time(s) of the sold items

    player.set_money(player.get_money() + total_earnings)
    player.inventory[item_name] -= quantity
    if player.inventory[item_name] == 0:
        del player.inventory[item_name]
    print(f"Sold {quantity} {item_name}(s) for ${total_earnings}.")
    show_balance()

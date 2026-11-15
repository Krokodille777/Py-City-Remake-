# Inventory management for the game
from main.player import player
items = ["item1", "item2", "item3"]

def add_item (item_name, quantity):
    if item_name in items:
        inv = player.get_inventory()
        inv[item_name] = inv.get(item_name, 0) + quantity
        player.set_inventory(inv)
        print(f"Added {quantity} of {item_name} to inventory.")
    else:
        print(f"{item_name} is not a valid item.")


def remove_item(item_name, quantity):
    if item_name in player.get_inventory():
        inv = player.get_inventory()
        if inv[item_name] >= quantity:
            inv[item_name] -= quantity
            if inv[item_name] == 0:
                del inv[item_name]
            player.set_inventory(inv)
            print(f"Removed {quantity} of {item_name} from inventory.")
        else:
            print(f"Not enough {item_name} in inventory to remove.")
    else:
        print(f"{item_name} not found in inventory.")

def check_inventory():
    if player.get_inventory():
        print("Current inventory:")
        for item, quantity in player.get_inventory().items():
            print(f"{item}: {quantity}")
    else:
        print("Inventory is empty.")

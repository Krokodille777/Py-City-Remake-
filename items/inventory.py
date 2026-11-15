# Inventory management for the game
items = ["item1", "item2", "item3"]

my_inventory = {}

def add_item (item_name, quantity):
    if item_name in items:
        if item_name in my_inventory:
            my_inventory[item_name] += quantity
        else:
            my_inventory[item_name] = quantity
        print(f"Added {quantity} of {item_name} to inventory.")
    else:
        print(f"{item_name} is not a valid item.")
    

def remove_item(item_name, quantity):
    if item_name in my_inventory:
        if my_inventory[item_name] >= quantity:
            my_inventory[item_name] -= quantity
            if my_inventory[item_name] == 0:
                del my_inventory[item_name]
            print(f"Removed {quantity} of {item_name} from inventory.")
        else:
            print(f"Not enough {item_name} in inventory to remove.")
    else:
        print(f"{item_name} not found in inventory.")

def check_inventory():
    if my_inventory:
        print("Current inventory:")
        for item, quantity in my_inventory.items():
            print(f"{item}: {quantity}")
    else:
        print("Inventory is empty.")

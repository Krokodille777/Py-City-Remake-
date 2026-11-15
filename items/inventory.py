# Inventory management for the game
from main.player import player

def check_inventory():
    if player.get_inventory():
        print("Current inventory:")
        for item, quantity in player.get_inventory().items():
            print(f"{item}: {quantity}")
    else:
        print("Inventory is empty.")

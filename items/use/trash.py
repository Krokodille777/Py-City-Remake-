from main.player import player

# Trash completely useless or expired items from the player's inventory.
# It'll bring no money back, but it will free up space in the inventory and prevent the player from consuming expired items.

def trash_item(item_name, quantity):
    if quantity <= 0:
        print("Invalid quantity. Please enter a positive integer.")
        return
    if player.inventory.get(item_name, 0) < quantity:
        print("Not enough items to trash.")
        return

    player.inventory[item_name] -= quantity
    if player.inventory[item_name] == 0:
        del player.inventory[item_name]
    print(f"Trashed {quantity} {item_name}(s).")
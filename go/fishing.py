from items.catalog import available
from main.player import player
import random

# Fishing logic
BIG_FISH = ["shark", "whale", "dolphin", "pike", "marlin", "treasure_chest", "salmon", "mackerel", "octopus"]

SMALL_FISH = ["tuna", "sardine", "anchovy", "herring", "cod", "trout", "catfish", "bass", "carp", "perch", "squid", "crab", "jellyfish", "boot"]


def use_bait():
    """Takes the best bait the player has. Returns its name, or None if there's no bait."""
    for bait_name in ["bait", "worm"]:            # best bait first
        if player.inventory.get(bait_name, 0) > 0:
            player.inventory[bait_name] -= 1
            if player.inventory[bait_name] <= 0:
                del player.inventory[bait_name]
            print(f"You put {bait_name} on the hook.")
            return bait_name
    return None


def catch_fish():
    if player.inventory.get("fishing_rod", 0) <= 0:
        print("You need a fishing rod to catch fish.")
        return
    bait_name = use_bait()
    if bait_name is None:
        print("You need a worm or bait to go fishing.")
        return

    print("You cast your line into the water...")
    big_chance = 0.7 if bait_name == "bait" else 0.3
    if random.random() < 0.01:
        catch = "treasure_chest"
    elif random.random() < big_chance:
        catch = random.choice(BIG_FISH)
    else:
        catch = random.choice(SMALL_FISH)

    player.inventory[catch] = player.inventory.get(catch, 0) + 1
    # adds it to the inventory and records the time, so fish can spoil
    print(f"You caught a {catch}!")
    player.set_happiness(min(100, player.get_happiness() + 5))  # Increase happiness by 5 points for catching a fish
    player.set_hunger(min(100, player.get_hunger() + 10))  # Increase hunger by 10 points for catching a fish
    player.set_luck(min(10, player.get_luck() + 0.5))  # Increase luck by 0.5 points for catching a fish

def treasure_chest():
    if player.inventory.get("treasure_chest", 0) <= 0:
        print("You don't have any treasure chests to open.")
        return

    player.inventory["treasure_chest"] -= 1
    if player.inventory["treasure_chest"] == 0:
        del player.inventory["treasure_chest"]

    # Randomly decide what the treasure chest contains
    contents = random.choices(
        population=["money", "item", "nothing"],
        weights=[0.5, 0.4, 0.1],  # Adjust probabilities as needed
        k=1
    )[0]

    if contents == "money":
        money_amount = random.randint(100, 1000)  # Random amount of money between 100 and 1000
        player.set_money(player.get_money() + money_amount)
        print(f"You opened the treasure chest and found ${money_amount}!")
    elif contents == "item":
        item_name = random.choice(list(available.keys()))
        player.inventory[item_name] = player.inventory.get(item_name, 0) + 1
        print(f"You opened the treasure chest and found a {item_name}!")
    else:
        print("You opened the treasure chest, but it was empty. Better luck next time!")

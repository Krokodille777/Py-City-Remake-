from items.catalog import available
from main.player import player
import random
import time

#Hunting Logic

# Use Hunting Rifle to hunt animals.
# To hunt an animal, the player needs to get ammo first (check 'bullet' in the shoplist)
# Each animal takes 1 bullet to hunt. If the player has no bullets, they cannot hunt.
# There is a chances of missing the target, whuch plays badly with the player's luck.
# Hunting trains endurance, luck, dexterity and perception skills

ANIMALS = ["rabbit", "deer", "boar", "bear", "fox", "wolf", 
                      "lynx", "moose", "bison", "raccoon", "hedgehog", 
                      "lion", "elephant", "tiger", "leopard", "cheetah", 
                      "crocodile", "rhino", "hippo", "zebra", "giraffe", 
                      "gorilla", "eagle", "falcon", "owl", "parrot", "vulture", 
                      "penguin", "polar_bear", "walrus"]

def use_bullet():
    """Takes a bullet from the player's inventory. Returns True if successful, False if no bullets are available."""
    if player.inventory.get("bullet", 0) > 0:
        player.inventory["bullet"] -= 1
        if player.inventory["bullet"] <= 0:
            del player.inventory["bullet"]
        print("You loaded a bullet into your hunting rifle.")
        return True
    else:
        print("You need bullets to hunt. Please buy some from the shop.")
        return False

def cooldown_hunting():
    """Cooldown for hunting. The player can hunt once every 10 minutes."""
    current_time = time.time()
    if current_time - player.last_hunted_time < 600:  # 600 seconds = 10 minutes
        remaining_time = 600 - (current_time - player.last_hunted_time)
        print(f"You need to wait {int(remaining_time)} seconds before hunting again.")
        return False
    return True 

def hunt_animal():
    if player.inventory.get("hunting rifle", 0) <= 0:
            print("You need a hunting rifle to hunt animals.")
            return
    if not use_bullet():
            return

    
    
    random_chance = random.random()  # Random chance for hunting success
    animal_name = random.choice(ANIMALS)  # Randomly select an animal to
    luck_factor = player.get_luck() / 10  # Assuming luck is a value
    success_chance = random_chance + luck_factor
    if success_chance > 0.5:
        player.inventory[animal_name] = player.inventory.get(animal_name, 0) + 1
        print(f"You successfully hunted a {animal_name}!")
        player.set_endurance(min(10, player.get_endurance() + 0.5))  # Increase endurance by 0.5 points for hunting
        player.set_luck(min(10, player.get_luck() + 0.2))  # Increase luck by 0.2 points for hunting
        player.set_dexterity(min(10, player.get_dexterity() + 0.3))  # Increase dexterity by 0.3 points for hunting
        player.set_perception(min(10, player.get_perception() + 0.4))  # Increase perception by 0.4 points for hunting
    else:
        print(f"You missed the {animal_name}. Better luck next time!")
        player.set_luck(max(0, player.get_luck() - 0.1))  # Decrease luck by 0.1 points for missing
    player.set_last_hunted_time(time.time())  # Update the last hunted time after hunting
    cooldown_hunting()  # Start the cooldown after hunting


from items.catalog import available
from main.player import player
import random
def chop_wood():
    axe_wood = random.randint(1, 3)  # Randomly determine how much wood is chopped
    chainsaw_wood = random.randint(3, 6)  # Chainsaw chops more wood
    if player.inventory.get("axe", 0) <= 0 and player.inventory.get("chainsaw", 0) <= 0:
        print("You need an axe or a chainsaw to chop wood.")
        return
    tool = input ("Which tool do you want to use? ([a]xe/[c]hainsaw): ").strip().lower()

    if tool == "c" and player.inventory.get("chainsaw", 0) > 0:
        if player.inventory.get("fuel", 0) <= 0:
            print("You need fuel to use the chainsaw.")
            return
    if player.get_energy() <= 20:
        print("You are too tired to chop wood. Rest or eat something to regain energy.")
        player.inventory["fuel"] -= 1
        print("You used the chainsaw to chop wood.")
        player.inventory["Wood"] = player.inventory.get("Wood", 0) + chainsaw_wood
        player.set_hunger(min(player.get_hunger() + 7, 100))  # Increase hunger by 5, max 100
        player.set_energy(min(player.get_energy() - 10, 100))  # Decrease energy by 10, min 0
        player.set_dexterity(min(player.get_dexterity() + 0.5, 100))  # Increase dexterity by 0.5, max 100
        player.set_endurance(min(player.get_endurance() + 0.5, 100))  # Increase endurance by 0.5, max 100
        print(f"You chopped {chainsaw_wood} pieces of wood.")

    elif tool == "a" and player.inventory.get("axe", 0) > 0:
        print("You used the axe to chop wood.")
        player.inventory["Wood"] = player.inventory.get("Wood", 0) + axe_wood
        player.set_hunger(min(player.get_hunger() + 15, 100))  # Increase hunger by 5, max 100
        player.set_energy(min(player.get_energy() - 30, 100))  # Decrease energy by 10, min 0
        player.set_dexterity(min(player.get_dexterity() + 1, 100))  # Increase dexterity by 0.5, max 100
        print(f"You chopped {axe_wood} pieces of wood.")

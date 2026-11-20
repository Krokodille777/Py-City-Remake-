from items.catalog import available
from main.player import player
import random

ORES = ["Iron", "Copper", "Silver", "Gold", "Platinum", "Diamond", "Emerald", "Ruby", "Sapphire", "Amethyst", 
        "Tin", "Lead", "Nickel", "Zinc", "Titanium", "Uranium", "Plutonium", "Manganese", "Chromium", "Aluminium",
        "Topaz", "Aquamarine", "Jewel", "Jade", "Opal", "Quartz", "Zircon", "Coal", "Salt", "Sulfur", "Sand",
        "Granite", "Chalk", "Clay", "Marble", "Gravel", "Oil", "Natural Gas"]

# Mining mostly brings ores and minerals, which can be used for crafting or sold for money. 
# Mining also trains endurance, and perception skills.
# But there is also a little chance to bring something except ores, like a treasure chest, or a completely random iten, even food.
# Most food found in mining is spoiled, but some are not. The player can eat them, or sell them for a small amount of money.


def mine_ore():
    if player.inventory.get("pickaxe", 0) <= 0:
        print("You need a pickaxe to mine ores.")
        return

    print("You swing your pickaxe and start mining...")
    random_chance = random.random()
    if random_chance < 0.1:  # 5% chance to find a treasure chest
        catch = "treasure_chest"
    elif random_chance < 0.25:  # 10% chance to find a random item
        catch = random.choice(list(available.keys()))
    else:
        catch = random.choice(ORES)

    player.inventory[catch] = player.inventory.get(catch, 0) + 1
    print(f"You mined a {catch}!")
    player.set_endurance(min(10, player.get_endurance() + 0.5))  # Increase endurance by 0.5 points for mining
    player.set_perception(min(10, player.get_perception() + 0.2))  # Increase perception by 0.2 points for mining


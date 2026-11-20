# Some activities that can be done with this item
# -- read: increases happiness and intelligence
# -- watch: a movie or show, or anime, increases happiness and perception
# -- play: a game or activity, increases happiness and luck
from items.catalog import available
from main.player import player

def read_item(item_name):
    item = available.get(item_name)
    if item is None:
        print(f"Unknown item '{item_name}'.")
        return
    
    if item ["type"] in ["book"]:
        if player.inventory.get(item_name, 0) <= 0:
            print(f"You don't have any {item_name} to read.")
            return

        player.inventory[item_name] -= 1
        if player.inventory[item_name] <= 0:
            del player.inventory[item_name]
        player.set_happiness(min(100, player.get_happiness() + available[item_name]["happiness"]))
        player.set_intelligence(min(10, player.get_intelligence() + available[item_name]["intelligence"]))
        print(f"You read {item_name}. Happiness: +{available[item_name]['happiness']}, Intelligence: +{available[item_name]['intelligence']}.")


def watch_item(item_name):
    # TV or smartphone required
    item = available.get(item_name)
    if item is None:
        print(f"Unknown item '{item_name}'.")
        return

    if item ["type"] in ["watch"] :
        if player.inventory.get(item_name, 0) <= 0:
            print (f"You don't have any {item_name} to watch.")
            return

        if player.inventory.get("TV", 0) <= 0 and player.inventory.get("smartphone", 0) <= 0:
            print("You need a TV or smartphone to watch this item.")
            return
        player.inventory[item_name] -= 1
        if player.inventory[item_name] <= 0:
            del player.inventory[item_name]

        player.set_happiness(min(100, player.get_happiness() + available[item]["happiness"]))
        player.set_perception(min(10, player.get_perception() + available[item]["perception"]))
        if "intelligence" in available[item]:
            player.set_intelligence(min(10, player.get_intelligence() + available[item]["intelligence"]))
        if "intelligence" in available[item]:
            print(f"Intelligence: +{available[item]['intelligence']}.")

        print(f"You watched {item}. Happiness: +{available[item]['happiness']}, Perception: +{available[item]['perception']}.")
        if "intelligence" in available[item]:
            print(f"You watched {item}. Happiness: +{available[item]['happiness']}, Perception: +{available[item]['perception']}, Intelligence: +{available[item]['intelligence']}.")


def play_item(item_name):
        item = available.get(item_name)
        if item is None:
            print(f"Unknown item '{item_name}'.")
            return
        if item["type"] != "play":
            print(f"You can't play {item_name}.")
            return
        if player.inventory.get(item_name, 0) <= 0:
            print(f"You don't have any {item_name} to play.")
            return

        if player.inventory.get("PC", 0) <= 0 and player.inventory.get("smartphone", 0) <= 0:
            print("You need a PC or smartphone to play this item.")
            return

        player.inventory[item_name] -= 1
        if player.inventory[item_name] <= 0:
            del player.inventory[item_name]

        gains = [f"Happiness: +{item.get('happiness', 0)}"]
        if "dexterity" in item:
            player.set_dexterity(min(10, player.get_dexterity() + item["dexterity"]))
            gains.append(f"Dexterity: +{item['dexterity']}")
        if "luck" in item:
            player.set_luck(min(10, player.get_luck() + item["luck"]))
            gains.append(f"Luck: +{item['luck']}")
        print(f"You played {item_name}. " + ", ".join(gains))


        
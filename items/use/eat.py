from items.catalog import available
from main.player import player
import time




#Each food and drink item has a shelf life in seconds. When the shelf time is over, the item becomes expired. 
#Consuming expired food or drink items will have negative effects on the player's health, energy, hunger and even happiness.
#Expired food or drink items are cheaper to sell. So it's better to consume them before they expire or just get rid of them by trashing them.
#When food or drink items are expired, they will be marked as "expired" in the player's inventory. The player can still consume them, but it will have negative effects on their stats.

def update_expired():
    now = time.time()
    for item_name, times in list(player.bought_at.items()):
        shelf_life = available[item_name]["shelf_life"]
        fresh = [t for t in times if now - t < shelf_life]
        expired_count = len(times) - len(fresh)

        if expired_count > 0:
            player.inventory[item_name] -= expired_count
            if player.inventory[item_name] <= 0:
                del player.inventory[item_name]
            expired_key = f"expired {item_name}"
            player.inventory[expired_key] = player.inventory.get(expired_key, 0) + expired_count
            print(f"{expired_count} {item_name}(s) went bad!")

        if fresh:
            player.bought_at[item_name] = fresh
        else:
            del player.bought_at[item_name]



def eat_item(item_name):
    quantity = 1
    is_expired = item_name.startswith("expired")
    item = available.get(item_name.removeprefix("expired "))
    times = player.bought_at.get(item_name, [])
    if item is None:
        print(f"Unknown item '{item_name}'.")
        return
    if item["type"] not in ["food", "drink", "seafood"]:
        print (f"Item '{item_name}' is not edible. Please spare your teeth and try something else.")
        return
    if item_name not in player.inventory or player.inventory[item_name] <= 0:
        print(f"You don't have any {item_name} to eat.")
        return
    player.inventory[item_name] -= quantity
    if player.inventory[item_name] <= 0:
        del player.inventory[item_name]
    del times[:quantity]  # forget the oldest purchase time(s) of the eaten item

    if is_expired:
        # Expired food still fills you up, but it hurts your health and mood and gives no energy.
        player.set_health(max(0, player.get_health() - abs(item["health"])))
        player.set_happiness(max(0, player.get_happiness() - 5))
        player.set_hunger(max(0, player.get_hunger() + item["hunger"]))
        print(f"You ate {item_name}. Yuck! Health: -{abs(item['health'])}, Happiness: -5, Hunger: {item['hunger']}.")
    else:
        player.set_health(min(100, player.get_health() + item["health"]))
        player.set_energy(min(100, player.get_energy() + item["energy"]))
        player.set_hunger(max(0, player.get_hunger() + item["hunger"]))
        print(f"You ate {item_name}. Health: +{item['health']}, Energy: +{item['energy']}, Hunger: {item['hunger']}.")
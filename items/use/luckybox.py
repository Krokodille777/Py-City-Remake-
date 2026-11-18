from items.catalog import available
from main.player import player
from money.balance import show_balance
import random

# When the lucky box is opened, there are 12 possible outcomes, six of which are pleasant and the rest six are not.
# You will never know what you will get. It really tricks your luck.
# Here are the possible oucomes (100 / 12 = 8.33% chance each):
# 1. Bunch of cheap items (2 - 4 items)
# 2. Bunch of expensive items (1 - 3 items)
# 3. Nothing (empty box)
# 4. Money that equals to the price of the lucky box
# 5. Doubling Crystal: dpubles your current balance
# 6. Magic Pill: heal 20 points, charge 20 points of energy, and decrease hunger by 20 points
# 7. Bad Apple: decrease health by 20 points
# 8. Weak Potion: decrease energy by 20 points
# 9. Rotten Meat: decrease hunger by 20 points
# 10. A Thief: steals some of your items (1 - 3 items)
# 11. Water Bomb: you lose some of your money (300 - 500)
# 12. Halving Crystal: you lose half of your current balance

# Good & neutral outcomes
def get_cheap_items():
    cheap_items = [item for item, details in available.items() if details["price"] <= 100]
    if not cheap_items:
        print("No cheap items available in the shop.")
        return
    num_items = random.randint(2, 4)
    item_names = random.sample(cheap_items, min(num_items, len (cheap_items)))
    print(f"You received {len(item_names)} cheap items.")
    player.set_happiness(min(100, player.get_happiness() + 5))  # Increase happiness by 5 points for receiving cheap items
    player.set_luck(min(10, player.get_luck() + 0.5))  # Increase luck by 0.5 points for receiving cheap items
    print("Your happiness has increased by 5 points for receiving cheap items.")
    print("Your luck has increased by 0.5 points for receiving cheap items.")
    return item_names

def get_expensive_items():
    expensive_items = [item for item, details in available.items() if details["price"] >= 500]
    if not expensive_items:
        print("No expensive items available in the shop.")
        return
    num_items = random.randint(1, 3)
    item_names = random.sample(expensive_items, min(num_items, len(expensive_items)))
    print(f"You received {len(item_names)} expensive items.")
    player.set_happiness(min(100, player.get_happiness() + 10))  # Increase happiness by 10 points for receiving expensive items
    player.set_luck(min(10, player.get_luck() + 1))  # Increase luck by 1 point for receiving expensive items
    print("Your happiness has increased by 10 points for receiving expensive items.")
    print("Your luck has increased by 1 point for receiving expensive items.")
    return item_names

def get_nothing():
    print("You opened the lucky box, but it was empty. Better luck next time!")
    player.set_happiness(max(0, player.get_happiness() - 5))  # Decrease happiness by 5 points
    player.set_luck(max(0, player.get_luck() - 1))  # Decrease luck by 1 point
    print("Your happiness has decreased by 5 points for receiving nothing.")
    return None

def get_luckybox_price():
    luckybox = available.get("lucky_box")
    if luckybox is None:
        print("Lucky box is not available in the shop.")
        return 0
    return luckybox["price"]

def get_doubled_balance():
    current_balance = player.get_money()
    player.set_money(current_balance * 2)
    print("Your balance has been doubled.")
    player.set_happiness(min(100, player.get_happiness() + 15))  # Increase happiness by 15 points for doubling balance
    player.set_luck(min(10, player.get_luck() + 1.5))  # Increase luck by 1.5 points for doubling balance
    print("Your happiness has increased by 15 points for doubling your balance.")
    print("Your luck has increased by 1.5 points for doubling your balance.")
    show_balance()

def magic_pill():
    player.set_health(min(100, player.get_health() + 20))
    player.set_energy(min(100, player.get_energy() + 20))
    player.set_hunger(max(0, player.get_hunger() - 20))
    print("You took the magic pill. Your health, energy, and hunger have been improved (20 points each).")
    player.set_happiness(min(100, player.get_happiness() + 10))  # Increase happiness by 10 points for taking magic pill
    player.set_luck(min(10, player.get_luck() + 1))  # Increase luck by 1 point for taking magic pill
    print("Your happiness has increased by 10 points for taking the magic pill.")
    print("Your luck has increased by 1 point for taking the magic pill.")

# Bad outcomes

def bad_apple():
    player.set_health(max(0, player.get_health() - 20))
    print("Oh no! You got a bad apple. Your health has decreased by 20 points.")
    player.set_happiness(max(0, player.get_happiness() - 10))  # Decrease happiness by 10 points for getting a bad apple
    player.set_luck(max(0, player.get_luck() - 1))
    print("Your happiness has decreased by 10 points for getting a bad apple.")
    print("Your luck has decreased by 1 point for getting a bad apple.")

def weak_potion():
    player.set_energy(max(0, player.get_energy() - 20))
    print("Oh no! You got a weak potion. Your energy has decreased by 20 points.")
    player.set_happiness(max(0, player.get_happiness() - 10))  # Decrease happiness by 10 points for getting a weak potion
    player.set_luck(max(0, player.get_luck() - 1))
    print("Your happiness has decreased by 10 points for getting a weak potion.")
    print("Your luck has decreased by 1 point for getting a weak potion.")

def rotten_meat():
    player.set_hunger(min(100, player.get_hunger() + 20))
    print("Oh no! You got rotten meat. Your hunger has increased by 20 points.")
    player.set_happiness(max(0, player.get_happiness() - 10))  # Decrease happiness by 10 points for getting rotten meat
    player.set_luck(max(0, player.get_luck() - 1))
    print("Your happiness has decreased by 10 points for getting rotten meat.")
    print("Your luck has decreased by 1 point for getting rotten meat.")

def thief():
    if not player.inventory:
        print("A thief tried to steal your items, but you have nothing to steal! Lucky you!")
        player.set_happiness(max(0, player.get_happiness() - 5))  # Decrease happiness by 5 points for encountering a thief
    else:
        num_items_to_steal = random.randint(1, min(3, len(player.inventory)))
        stolen_items = random.sample(list(player.inventory.keys()), num_items_to_steal)
        for item in stolen_items:
            del player.inventory[item]
        print(f"A thief stole {num_items_to_steal} of your items: {', '.join(stolen_items)}.")
        player.set_happiness(max(0, player.get_happiness() - 15))  # Decrease happiness by 15 points for losing items to a thief
        player.set_luck(max(0, player.get_luck() - 2))  # Decrease luck by 2 points for losing items to a thief
        print("Your happiness has decreased by 15 points for losing items to a thief.")
        print("Your luck has decreased by 2 points for losing items to a thief.")

def water_bomb():
    money_lost = random.randint(300, 500)
    current_balance = player.get_money()
    if current_balance < money_lost:
        money_lost = current_balance  # Lose all money if not enough
    player.set_money(current_balance - money_lost)
    print(f"You got hit by a water bomb. You lost ${money_lost}.")
    player.set_happiness(max(0, player.get_happiness() - 10))  # Decrease happiness by 10 points for losing money to a water bomb
    player.set_luck(max(0, player.get_luck() - 1))  # Decrease luck by 1 point for losing money to a water bomb
    print("Your happiness has decreased by 10 points for losing money to a water bomb.")
    print("Your luck has decreased by 1 point for losing money to a water bomb.")
    show_balance()

def halving_crystal():
    current_balance = player.get_money()
    money_lost = current_balance // 2
    player.set_money(current_balance - money_lost)
    print(f"You got a halving crystal. You lost half of your balance: ${money_lost}.")
    player.set_happiness(max(0, player.get_happiness() - 15))  # Decrease happiness by 15 points for losing half of the balance
    player.set_luck(max(0, player.get_luck() - 3))  # Decrease luck by 3 points for losing half of the balance
    print("Your happiness has decreased by 15 points for losing half of your balance.")
    print("Your luck has decreased by 3 points for losing half of your balance.")
    show_balance()


# Open the box

def open_lucky_box():
    if player.inventory.get("lucky_box", 0) <= 0:
        print("You don't have any lucky boxes to open.")
        return
    player.inventory["lucky_box"] -= 1
    if player.inventory["lucky_box"] == 0:
        del player.inventory["lucky_box"]
    print("You opened the lucky box. Let's see what you got...")
    match random.randint(1, 12):
        case 1:
            item_names = get_cheap_items()
            if item_names:
                for item_name in item_names:
                    player.inventory[item_name] = player.inventory.get(item_name, 0) + 1
        case 2:
            item_names = get_expensive_items()
            if item_names:
                for item_name in item_names:
                    player.inventory[item_name] = player.inventory.get(item_name, 0) + 1
        case 3:
            get_nothing()
        case 4:
            luckybox_price = get_luckybox_price()
            player.set_money(player.get_money() + luckybox_price)
            print(f"You received ${luckybox_price} from the lucky box.")
        case 5:
            get_doubled_balance()
        case 6:
            magic_pill()
        case 7:
            bad_apple()
        case 8:
            weak_potion()
        case 9:
            rotten_meat()
        case 10:
            thief()
        case 11:
            water_bomb()
        case 12:
            halving_crystal()

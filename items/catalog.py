available = {
    "apple" : {"price" : 2, "type": "food", "health": 5, "energy": 10, "shelf_life": 5, "hunger": -2},
    "orange" : {"price" : 3, "type": "food", "health": 7, "energy": 12, "shelf_life": 300, "hunger": -3},
    "coffee" : {"price" : 8, "type": "drink", "health": 0, "energy": 20, "shelf_life": 600, "hunger": -1},
    "banana" : {"price" : 2, "type": "food", "health": 6, "energy": 15, "shelf_life": 300, "hunger": -2},
    "potato" : {"price" : 1, "type": "food", "health": 4, "energy": 8, "shelf_life": 300, "hunger": -1},
    "bread" : {"price" : 3, "type": "food", "health": 8, "energy": 15, "shelf_life": 600, "hunger": -7},
    "wine" : {"price" : 10, "type": "drink", "health": -5, "energy": 5, "shelf_life": 3600, "hunger": 0},
    "water" : {"price" : 1, "type": "drink", "health": 0, "energy": 5, "shelf_life": 3600, "hunger": 0},
    "hotdog" : {"price" : 25, "type": "food", "health": 10, "energy": 20, "shelf_life": 600, "hunger": -9},
    "burger" : {"price" : 30, "type": "food", "health": 15, "energy": 25, "shelf_life": 600, "hunger": -12},
    "tomato" : {"price" : 2, "type": "food", "health": 5, "energy": 10, "shelf_life": 300, "hunger": -2},
    "lettuce" : {"price" : 2, "type": "food", "health": 5, "energy": 10, "shelf_life": 300, "hunger": -2},
    "chocolate" : {"price" : 15, "type": "food", "health": 5, "energy": 15, "shelf_life": 600, "hunger": -5},
    "energy_drink" : {"price" : 30, "type": "drink", "health": -5, "energy": 50, "shelf_life": 3600, "hunger": 0},
    "beer" : {"price" : 12, "type": "drink", "health": -10, "energy": 10, "shelf_life": 3600, "hunger": 0},
    "cake" : {"price" : 40, "type": "food", "health": 10, "energy": 30, "shelf_life": 600, "hunger": -17},
    "pizza" : {"price" : 25, "type": "food", "health": 15, "energy": 35, "shelf_life": 600, "hunger": -20},
    "house" : {"price" : 5000, "type": "booster", "happiness": 20, "desc": "A house boosts your happiness and salary when working. It can also give you a place to sleep.    "},
    "car" : {"price" : 2500, "type": "booster", "happiness": 10, "desc": "A car allows you to travel to nearby cities without a ticket. It also boosts your happiness and salary when working. Technically, it can also give you a place to sleep, but it's not recommended."},
    "diamomd": {"price" : 1000, "type": "collectible", "desc": "A shiny thing everyone wants. Be careful, though. You'll become wanted by thieves and criminals if you have it. It boosts your happiness and salary when working. It can also give you a place to sleep."},
    "emerald": {"price" : 1500, "type": "collectible", "desc": "The same as a diamond, but more expensive."},
    "ruby": {"price" : 2000, "type": "collectible", "desc": "The same as a diamond, but even more expensive."},
    "lucky_box" : {"price" : 120, "type": "usable", "desc": "A box that tests your luck. You'll never know what you'll get. From money and jewels, to bombs and curses, this box has everything to make you cherish it or regret it. Good luck! >:)"},
    "gift_box": {"price": 250, "type": "usable", "desc": "A box containing a random item available in the shop. It can be a food, drink, booster, collectible, or usable item. You never know what you'll get!"},
}

def show_shoplist():
    print("Available items in the shop:")
    for item, details in available.items():
        if "desc" in details:
            print(f"- {item}: ${details['price']} ({details['type']}) - {details['desc']}")
        elif details["type"] in ["food", "drink"]:
            print(f"- {item}: ${details['price']} ({details['type']}) - Health: {details['health']}, Energy: {details['energy']}, Shelf Life: {details['shelf_life']} seconds")
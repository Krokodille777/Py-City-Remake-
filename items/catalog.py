available = {
    "apple": 10,
    "orange": 15,
    "banana": 5,
    "kiwi": 20,
    "diamond": 1000
}

def show_shoplist():
    print("Available items in the shop:")
    for item, price in available.items():
        print(f"{item}: ${price}")

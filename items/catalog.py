available = {
    "apple": 10,
    "orange": 15,
    "banana": 5,
    "kiwi": 20,
    "coffee": 25,
    "hotdog": 30,
    "burger": 50,
    "diamond": 1000,
    "house": 5000,
    "car": 2000,
}

def show_shoplist():
    print("Available items in the shop:")
    for item, price in available.items():
        print(f"{item}: ${price}")

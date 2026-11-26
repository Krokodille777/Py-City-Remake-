# A catalogue for cooked food and crafted items.
# The main difference between them is that
# you can't find cooked food in the shoplist. They can only be obtained by cooking, respectively.
# They cannot be sold too.

dishes_available = {
    "dough": {"ingredients": {"flour": 2, "water": 1, "egg": 1, "sunflower_oil": 1}, "health": 5, "energy": 10, "hunger": -5, "shelf_life": 200},
    "bacon": {"ingredients": {"pork": 2, "salt": 1, "pepper": 1}, "health": 10, "energy": 15, "hunger": -8, "shelf_life": 300},
    "ketchup": {"ingredients": {"tomato": 3, "sugar": 1, "salt": 1}, "health": 5, "energy": 10, "hunger": -5, "shelf_life": 1000},
    "mayonnaise": {"ingredients": {"egg": 2, "sunflower_oil": 2, "mustard": 1}, "health": 5, "energy": 10, "hunger": -5, "shelf_life": 1000},
    "fried_egg": {"ingredients": {"egg": 1, "sunflower_oil": 1}, "health": 10, "energy": 12, "hunger": -8, "shelf_life": 200},
    "homemade_bread": {"ingredients": {"flour": 2, "water": 1, "yeast": 1}, "health": 12, "energy": 15, "hunger": -10, "shelf_life": 300},
    "fried_egg_n_bacon": {"ingredients": {"fried_egg": 1, "bacon": 2}, "health": 15, "energy": 20, "hunger": -12, "shelf_life": 300},
    "fruit_salad": {"ingredients": {"banana": 1, "orange": 1, "kiwi": 1, "carrot": 1}, "health": 15, "energy": 20, "hunger": -12, "shelf_life": 250},
    "pork_meatballs": {"ingredients": {"pork": 2, "onion": 1, "garlic": 1, "cabbage": 1}, "health": 20, "energy": 25, "hunger": -15, "shelf_life": 400},
    "homemade_pizza": {"ingredients": {"dough": 1, "tomato": 2, "cheese": 1, "salami": 1, "mushroom": 1}, "health": 25, "energy": 30, "hunger": -20, "shelf_life": 500},
    "pasta": {"ingredients": {"dough": 1, "water": 1, "salt": 1}, "health": 20, "energy": 25, "hunger": -15, "shelf_life": 400},
    "apple_pie": {"ingredients": {"dough": 1, "apple": 2, "sugar": 1, "cinnamon": 1}, "health": 30, "energy": 35, "hunger": -25, "shelf_life": 600},
    "fish_chips": {"ingredients": {"trout": 1, "perch": 1, "bass": 1, "sunflower_oil": 1, "salt": 1}, "health": 25, "energy": 30, "hunger": -20, "shelf_life": 500},
    "spaghetti_bolognese": {"ingredients": {"pasta": 1, "beef": 2, "tomato": 2, "onion": 1, "garlic": 1, "salt": 1, "black_pepper": 1}, "health": 35, "energy": 40, "hunger": -25, "shelf_life": 700},
    "homemade_hotdog": {"ingredients": {"dough": 1, "sausage": 1, "ketchup": 1, "mustard": 1}, "health": 20, "energy": 25, "hunger": -15, "shelf_life": 400},
    "homemade_burger": {"ingredients": {"dough": 1, "beef": 2, "cheese": 1, "lettuce": 1, "tomato": 1, "ketchup": 1, "mustard": 1, "onion": 1}, "health": 30, "energy": 35, "hunger": -25, "shelf_life": 600},
    "homemade_wine" : {"ingredients": {"grape": 5, "sugar": 2, "water": 1}, "health": -10, "energy": 30, "hunger": -5, "shelf_life": 1000},
    "homemade_steak": {"ingredients": {"beef": 3, "salt": 1, "black_pepper": 1}, "health": 40, "energy": 50, "hunger": -30, "shelf_life": 800},
    "homemade_stew": {"ingredients": {"beef": 2, "carrot": 1, "potato": 1, "onion": 1, "garlic": 1, "cabbage": 1, "salt": 1, "black_pepper": 1}, "health": 35, "energy": 40, "hunger": -25, "shelf_life": 700},
    "mashed_potatoes": {"ingredients": {"potato": 3, "butter": 1, "milk": 1, "salt": 1}, "health": 20, "energy": 25, "hunger": -15, "shelf_life": 400},
    "mushroom_soup": {"ingredients": {"mushroom": 3, "onion": 1, "garlic": 1, "potato": 1, "salt": 1, "black_pepper": 1}, "health": 25, "energy": 30, "hunger": -20, "shelf_life": 500},
    "pancakes": {"ingredients": {"flour": 2, "egg": 1, "milk": 1, "sugar": 1, "butter": 1}, "health": 20, "energy": 25, "hunger": -15, "shelf_life": 400},
    "grilled_chicken": {"ingredients": {"chicken": 2, "salt": 1, "black_pepper": 1, "sunflower_oil": 1}, "health": 30, "energy": 35, "hunger": -25, "shelf_life": 600},
    "bowl_of_rice": {"ingredients": {"rice": 2, "water": 1, "salt": 1}, "health": 15, "energy": 20, "hunger": -10, "shelf_life": 300},
    "noodles_chicken_chilli": {"ingredients": {"dough": 2, "chicken": 1, "chilli_pepper": 1, "garlic": 1, "salt": 1}, "health": 25, "energy": 30, "hunger": -20, "shelf_life": 500},
    "sauerkraut": {"ingredients": {"cabbage": 2, "salt": 1}, "health": 15, "energy": 20, "hunger": -10, "shelf_life": 1000},
}

crafted_items_available = {
    #Items Number 1
    "nails": {"ingredients": {"Iron": 1}, "desc": "Nails are used to build furniture and other items. One Iron = 10 nails."},
    "fabric": {"ingredients": {"cotton": 2}, "desc": "Fabric is used to make clothes and other items."},
    "steel": {"ingredients": {"Iron": 2, "Coal": 1}, "desc": "Steel is used to make tools and other items."},
    "powder": {"ingredients": {"Sulfur": 1, "Coal": 1}, "desc": "Gunpowder is used to make explosives and other items."},
    "string": {"ingredients": {"cotton": 1}, "desc": "String is used to make clothes and other items."},
    "paper": {"ingredients": {"wood": 1}, "desc": "Paper is used to make books and other items."},
    "glass": {"ingredients": {"Sand": 2}, "desc": "Glass is used to make windows and other items."},
    "bronze": {"ingredients": {"Copper": 2, "Tin": 1}, "desc": "Bronze is used to make tools and other items."},
    "ceramic": {"ingredients": {"Clay": 2}, "desc": "Ceramic is used to make dishes and other items."},
    # furniture
    "chair": {"ingredients": {"wood": 1, "nail": 6}, "desc": "A chair is a piece of furniture that allows you to sit."},
    "table": {"ingredients": {"wood": 2, "nail": 4}, "desc": "A table is a piece of furniture that allows you to put things on it."},
    "bed": {"ingredients": {"wood": 3, "nail": 10, "fabric": 5}, "desc": "A bed is a piece of furniture that allows you to sleep."},
    "sofa": {"ingredients": {"wood": 3, "nail": 7, "fabric": 10}, "desc": "A sofa is a piece of furniture that allows you to sit and relax."},
    "closet": {"ingredients": {"wood": 4, "nail": 30, "fabric": 15}, "desc": "A closet is a piece of furniture that allows you to store clothes and other items."},
    "shelf": {"ingredients": {"wood": 2, "nail": 12}, "desc": "A shelf is a piece of furniture that allows you to store items."},
    # tools 
    "axe": {"ingredients": {"wood": 5, "nail": 5, "steel": 2}, "desc": "A homemade axe is a tool that allows you to chop wood."},
    "pickaxe": {"ingredients": {"wood": 5, "nail": 5, "steel": 2}, "desc": "A homemade pickaxe is a tool that allows you to mine ores and gems."},
    "bait": {"ingredients": {"worm": 1, "fabric": 1}, "desc": "Bait is used to catch fish."},
    "bullet": {"ingredients": {"powder": 1, "Lead": 1}, "desc": "Bullets are used to shoot animals and other targets."},
    "fishing_rod": {"ingredients": {"wood": 5, "nail": 5, "string": 2}, "desc": "A fishing rod is a tool that allows you to catch fish."},
    "hunting_rifle": {"ingredients": {"wood": 5, "nail": 5, "steel": 2}, "desc": "A hunting rifle is a tool that allows you to hunt animals."},
    # other items
    "book": {"ingredients": {"paper": 5, "fabric": 1}, "desc": "A book is an item that allows you to read and learn new things."},
    "lamp": {"ingredients": {"wood": 10, "nail": 20, "steel": 5, "Copper": 2}, "desc": "A lamp is a tool that provides light."},
}
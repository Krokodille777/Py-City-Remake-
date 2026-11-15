import json
from main.player import player

SAVE_FILE = "pycity_save.json"

def save_game():
    with open(SAVE_FILE, "w", encoding="utf-8") as file:
        json.dump(player.to_dict(), file, indent=4)
    print("Game saved.")

def load_game():
    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
        player.load_from_dict(data)
        print("Game loaded.")
    except FileNotFoundError:
        print("No save file found.")
    except (json.JSONDecodeError, KeyError):
        print("Save file is damaged and can't be loaded.")
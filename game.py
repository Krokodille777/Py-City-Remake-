# Main file of the game. Physics and game logic will be imported here. This fille will handle, starting the game, game process, command list and end of the game.
import enum
from items.inventory import check_inventory
from items.catalog import show_shoplist
from items.use.eat import eat_item, update_expired
from items.use.giftbox import open_gift_box
from items.use.luckybox import open_lucky_box
from items.use.trash import trash_item
from items.use.leisure import read_item, watch_item, play_item
from main.save_and_load import save_game, load_game
from main.player import player
from main.check_time import check_time
from money.balance import show_balance
from money.trade import buy_item, sell_item
from money.work import work, sleep
from money.gamble import gamble
from go.fishing import catch_fish, treasure_chest
from go.hunting import hunt_animal
from go.mining import mine_ore
class GameState(enum.Enum):
    START = 1
    PLAYING = 2
    PAUSED = 3
    GAME_OVER = 4


command_list = ("balance","help", "play", "save", "load", "exit", "pause", "resume", 
                "inventory", "buy", "sell", "shoplist", "health", "energy", "happiness", 
                "work", "sleep", "eat", "hunger", "open", "trash", "luck", "status", 
                "read", "watch", "game", "fish", "hunt", "mine", "gamble", "time") #add_item and remove_item are temporary commands. They're here to test the inventory system. They'll be replaced with buy, sell, trash and use commands in the future.

def print_help():
    print("Available commands:")
    for command in command_list:
        print(f"- {command}")
def main():
    game_state = GameState.START
    print("Welcome to the game!")
    while True:
        if game_state == GameState.START:
           
            command = input ("Enter play to start the game. Or type 'exit' to quit: ")
            if command == "play":
                game_state = GameState.PLAYING
            elif command == "exit":
                print("Exiting the game. Goodbye!")
                break
            else:
                print(f"Unknown command: {command}. Type 'help' for a list of commands.")

        elif game_state == GameState.PLAYING:
            print("Game is now playing...")
            command = input("Enter a command (type 'help' for a list of commands): ")
            update_expired()  # Update expired items before processing commands
            if command == "pause":
                game_state = GameState.PAUSED
                print("Game paused. Type 'resume' to continue.")
            elif command == "resume":
                game_state = GameState.PLAYING
                print("Game resumed.")
            elif command == "help":
                print_help()
            elif command == "exit":
                print("Exiting the game. Goodbye!")
                break
            elif command == "balance":
                show_balance()
            elif command == "inventory":
                check_inventory()
            elif command == "save":
                save_game()
            elif command == "load":
                load_game()
            elif command == "buy":
                item_name = input("Enter the item name to buy: ")
                quantity = int(input("Enter the quantity to buy: "))
                buy_item(item_name, quantity)
            elif command == "sell":
                item_name = input("Enter the item name to sell: ")
                quantity = int(input("Enter the quantity to sell: "))
                sell_item(item_name, quantity)
            elif command == "shoplist":
                show_shoplist()
            elif command == "health":
                print(f"Your current health is: {player.get_health()}")
            elif command == "energy":
                print(f"Your current energy is: {player.get_energy()}")
            elif command == "happiness":
                print(f"Your current happiness is: {player.get_happiness()}")
            elif command == "work":
                work()
            elif command == "sleep":
                sleep()
            elif command == "eat":
                item_name = input("Enter the item name to eat: ")
                eat_item(item_name)
            elif command == "hunger":
                print(f"Your current hunger level is: {player.get_hunger()}")
            elif command == "trash":
                item_name = input("Enter the item name to trash: ")
                quantity = int(input("Enter the quantity to trash: "))
                trash_item(item_name, quantity)
            elif command == "open":
                box_input = input("Enter the box type to open (gift_box or lucky_box): ")
                if box_input == "gift_box":
                    open_gift_box()
                elif box_input == "lucky_box":
                    open_lucky_box()
                elif box_input == "treasure_chest":
                    treasure_chest()
                else:
                    print("Invalid box type.")
            elif command == "luck":
                print(f"Your current luck is: {player.get_luck()}")
            elif command == "status":
                status = player.player_status()
                for key, value in status.items():
                    print(f"{key}: {value}")
            elif command == "read":
                item_name = input("Enter the item name to read: ")
                read_item(item_name)
            elif command == "watch":
                item_name = input("Enter the item name to watch: ")
                watch_item(item_name)
            elif command == "game":
                item_name = input("Enter the item name to play: ")
                play_item(item_name)
            elif command == "fish":
                catch_fish()
            elif command == "hunt":
                hunt_animal()
            elif command == "mine":
                mine_ore()
            elif command == "gamble":
                gamble()
            elif command == "time":
                check_time()
            else:
                print(f"Unknown command: {command}. Type 'help' for a list of commands.")

        elif game_state == GameState.PAUSED:
            print("Game is paused.")
            command = input("Game is paused. Type 'resume' to continue or 'exit' to quit: ")
            if command == "resume":
                game_state = GameState.PLAYING
                print("Game resumed.")
            elif command == "exit":
                print("Exiting the game. Goodbye!")
                break
        
if __name__ == "__main__":
    main()
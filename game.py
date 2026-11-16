# Main file of the game. Physics and game logic will be imported here. This fille will handle, starting the game, game process, command list and end of the game.
import enum
from money.balance import show_balance
from items.inventory import check_inventory
from items.catalog import show_shoplist
from main.save_and_load import save_game, load_game
from money.trade import buy_item, sell_item
from main.player import player
from money.work import work, sleep
class GameState(enum.Enum):
    START = 1
    PLAYING = 2
    PAUSED = 3
    GAME_OVER = 4


command_list = ("balance","help", "play", "save", "load", "exit", "pause", "resume", "inventory", "buy", "sell", "shoplist", "health", "energy", "happiness", "work", "sleep") #add_item and remove_item are temporary commands. They're here to test the inventory system. They'll be replaced with buy, sell, trash and use commands in the future.

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
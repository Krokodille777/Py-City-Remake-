# Main file of the game. Physics and game logic will be imported here. This fille will handle, starting the game, game process, command list and end of the game.
import enum
from money.balance import show_balance
from items.inventory import add_item, remove_item, check_inventory
class GameState(enum.Enum):
    START = 1
    PLAYING = 2
    PAUSED = 3
    GAME_OVER = 4
command_list = ("balance","help", "play", "exit", "pause", "resume", "inventory", "add_item", "remove_item") #add_item and remove_item are temporary commands. They're here to test the inventory system. They'll be replaced with buy, sell, trash and use commands in the future.

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
            elif command == "add_item":
                item_name = input("Enter the name of the item to add: ")
                quantity = int(input("Enter the quantity to add: "))

                if quantity.is_integer() and quantity > 0:
                    add_item(item_name, quantity)
                else:
                    print("Invalid quantity. Please enter a positive integer.")

                
            elif command == "remove_item":
                item_name = input("Enter the name of the item to remove: ")
                quantity = int(input("Enter the quantity to remove: "))
                if quantity.is_integer() and quantity > 0:
                    remove_item(item_name, quantity)
                else:
                    print("Invalid quantity. Please enter a positive integer.")
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
# Main file of the game. Physics and game logic will be imported here. This fille will handle, starting the game, game process, command list and end of the game.
import enum

class GameState(enum.Enum):
    START = 1
    PLAYING = 2
    PAUSED = 3
    GAME_OVER = 4

command_list = ("help", "play", "exit", "pause", "resume")

def print_help():
    print("Available commands:")
    for command in command_list:
        print(f"- {command}")
def main():
    game_state = GameState.START
    while True:
        if game_state == GameState.START:
            print("Welcome to the game!")
            command = input ("Enter play to start the game ")
            if command == "play":
                game_state = GameState.PLAYING
            else: 
                print("Invalid command. Type 'play' to start the game.")

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
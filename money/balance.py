# Check user's balance in the game
from  main.player  import Player

player1 = Player(100, {})  # Initialize Player1 with a starting balance of $100 and an empty inventory
def show_balance():
    current_balance = player1.get_money()
    print(f"Your current balance is: ${current_balance}")
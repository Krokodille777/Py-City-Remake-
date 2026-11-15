# Check user's balance in the game
from  main.player  import player
def show_balance():
    current_balance = player.get_money()
    print(f"Your current balance is: ${current_balance}")
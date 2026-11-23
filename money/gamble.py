from gambling import battle, coinflip, random_number, rps, slotmachine

from main.player import player

# Gamble rules:
# Gambling requires special tokens that are available in the store.
# To start gambling, insert a token and choose a game to play.
# Each game has its own rules and payouts, which are explained in the game itself.
# Good luck! I hope you don't lose all your money. This ain't Las Vegas.

def insert_token():
    if player.inventory.get("gambling_token", 0) <= 0:
        print("You don't have any gambling tokens. You can buy them in the store.")
        return False
    else:
        player.inventory["gambling_token"] -= 1
        print("You inserted a gambling token. You can now play a game.")
        if player.inventory["gambling_token"] == 0:
            del player.inventory["gambling_token"]
        return True
        
    

def gamble():
    if not insert_token():
        return
    print("Welcome to the casino! You can play the following games:")
    print("1. Rock, Paper, Scissors")
    print("2. Coin Flip")
    print("3. Guess a Number")
    print("4. Battle")
    print("5. Slot Machine")
    game_choice = input("Choose a game to play (1-5): ")
    if game_choice == "1":
        bid_amount = int(input("Enter your bid amount: "))
        rps.rock_paper_scissors(bid_amount)
    elif game_choice == "2":
        bid_amount = int(input("Enter your bid amount: "))
        coinflip.coinflip(bid_amount)
    elif game_choice == "3":
        bid_amount = int(input("Enter your bid amount: "))
        random_number.guess_number(bid_amount)
    elif game_choice == "4":
        bid_amount = int(input("Enter your bid amount: "))
        battle.battle(bid_amount)
    elif game_choice == "5":
        bid_amount = int(input("Enter your bid amount: "))
        slotmachine.pull_lever(bid_amount)
    else:
        print("Invalid choice. Please choose a valid game.")
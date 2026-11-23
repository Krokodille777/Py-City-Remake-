from main.player import player
import time

# Check the current time.
# Checking time requires the player to have a clock or a smartphone in their inventory.
#  If the player has a clock or a smartphone, they can check the current time. 
# If not, they will be informed that they need to have a clock or a smartphone to check the time.

def check_time():
    if "clock" in player.inventory or "smartphone" in player.inventory:
        current_time = time.strftime("%H:%M:%S", time.localtime())
        print(f"The current time is: {current_time}")
    else:
        print("You need to have a clock or a smartphone in your inventory to check the time.")
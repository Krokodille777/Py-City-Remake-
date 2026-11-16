from main.player import player, WorkState
from money.balance import show_balance
import random
import time


BOOSTERS = ["house", "car"]
COOLDOWN_SECONDS = 5

def salary():
    earned = random.randint(100, 500)  
    inventory = player.get_inventory()
    if "house" in inventory and "car" in inventory:
        earned *= 3
    elif "house" in inventory:
        earned *= 2
    elif "car" in inventory:
        earned *= 2
    player.set_money(player.get_money() + earned)

#if player gets a high salary, their happines will increase. Otherwise, it will decrease. The threshold for a high salary is set at $300.
    if earned >= 300:
        player.set_happiness(player.get_happiness() + 10)
        print ("You earned a high salary, so your happiness has increased by 10 points.")
    else:
        player.set_happiness(player.get_happiness() - 5)
        print ("You didn't earn a high salary, so your happiness has decreased by 5 points.")
    return earned



def exhaustion():
    r2 = random.choice([10, 20, 30, 40, 50])  # Random exhaustion between 10 and 50
    match r2:
        case 10:
            print ("You are feeling a bit tired. Your energy has decreased by 10.")
        case 20:
            print ("You are feeling tired. Your energy has decreased by 20.")
        case 30:
            print ("You are feeling very tired. Your energy has decreased by 30.")
        case 40:
            print ("You are feeling exhausted. Your energy has decreased by 40.")
        case 50:
            print ("You are feeling extremely exhausted. Your energy has decreased by 50.") 
    if player.get_energy() - r2 < 0:
        player.set_energy(0)
        player.set_health(max(0, player.get_health() - 10))
        player.set_happiness (max(0, player.get_happiness() - 10))
        print ("Warning! Energy Level Critical! Get rest immediately!")
    player.set_energy(max(0, player.get_energy() - r2))
    print (f"You are feeling tired. Your energy has decreased by {r2}.")




def work():
    if player.get_work_state() == WorkState.DONE:
        remaining = COOLDOWN_SECONDS - (time.time() - player.last_work_time)
        if remaining > 0:
            print(f"You need to rest before working again. Wait {int(remaining) + 1} more seconds.")
            return
        player.set_work_state(WorkState.READY)

    print("You are going to work...")
    time.sleep(2)  # simulate the shift
    exhaustion()
    earned = salary()
    print(f"Your shift is over. You earned ${earned}.")
    show_balance()
    player.set_work_state(WorkState.DONE)
    player.last_work_time = time.time()




def sleep():
    print("You are going to sleep...")
    if player.get_energy () == 100:
        print ("You are already fully rested. You don't need to sleep.")
        return
    while player.get_energy() < 100:
        time.sleep(2) # Simulate time taken to sleep
        print("Zzzzz...")
        player.set_energy(min(100, player.get_energy() + 10))
        print(f"You slept for a while. Your energy has increased by 10. Current energy: {player.get_energy()}")
    player.set_energy(min(100, player.get_energy() + 50))
    print ("You have slept well. Your energy has increased by 50.")
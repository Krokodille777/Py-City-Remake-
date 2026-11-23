#The unique type of gambling game:
#Game rules:
#You fight the computer in a battle.
#You can choose between 6 different attacks:
#punch, parry, dodge, kick, lunge and dive.

#punch beat punch and lunge,
#parry beats punch and lunge,
#dodge beats punch and kick,
#kick beats punch and parry,
#lunge beats kick and dodge,
#dive beats lunge.
#players get 20 health and 10 energy at the start of the game.
#the game ends when either the player or the computer runs out of health.
#parry, dodge and dive restore energy, while punch, kick and lunge use it.

#critical hits can happen, which will deal double damage to the opponent.
#they happen randomly, and the chance of them happening is based on the player's luck stat.

from main.player import player
import random

START_HEALTH = 20
START_ENERGY = 10
MAX_ENERGY = 10
WIN_MULTIPLIER = 2  # how many times the bid you get back when you win

# energy_cost < 0 means the move restores energy.
# "beats" lists the moves this move wins against. If two moves beat each other, both fighters get hit.
ATTACKS = {
    "punch": {"damage": 5,  "energy_cost": 2,  "beats": ["punch", "lunge", "dive"]},
    "parry": {"damage": 0,  "energy_cost": -1, "beats": ["punch", "lunge"]},
    "dodge": {"damage": 0,  "energy_cost": -1, "beats": ["punch", "kick"]},
    "kick":  {"damage": 7,  "energy_cost": 3,  "beats": ["punch", "parry"]},
    "lunge": {"damage": 8,  "energy_cost": 4,  "beats": ["kick", "dodge"]},
    "dive":  {"damage": 10, "energy_cost": 5,  "beats": ["lunge", "kick"]},
}


def bid(amount):
    if amount <= 0:
        print("The bid must be a positive number.")
        return False
    if amount > player.money:
        print("You don't have enough money to bid that amount.")
        return False
    player.money -= amount
    print(f"You bid ${amount}.")
    return True


def affordable_moves(energy):
    return [name for name, move in ATTACKS.items() if move["energy_cost"] <= energy]


def hit(attacker_name, move_name):
    """Returns the damage of a successful hit. Critical hits (double damage) depend on the player's luck."""
    damage = ATTACKS[move_name]["damage"]
    if damage == 0:
        return 0
    crit_chance = 0.05 + player.get_luck() * 0.01 if attacker_name == "You" else 0.1
    if random.random() < crit_chance:
        print(f"CRITICAL HIT by {attacker_name}!")
        damage *= 2
    return damage


def battle(bid_amount):
    if not bid(bid_amount):
        return

    player_health, player_energy = START_HEALTH, START_ENERGY
    computer_health, computer_energy = START_HEALTH, START_ENERGY
    round_number = 1

    while player_health > 0 and computer_health > 0:
        print()
        print(f"--- Round {round_number} ---")
        print(f"You: {player_health} HP, {player_energy} energy | Computer: {computer_health} HP, {computer_energy} energy")

        moves = affordable_moves(player_energy)
        player_move = input(f"Choose your move ({', '.join(moves)}): ").strip().lower()
        if player_move not in ATTACKS:
            print("Unknown move. Try again.")
            continue
        if player_move not in moves:
            print(f"Not enough energy for {player_move}. Try a defensive move to recover.")
            continue

        computer_move = random.choice(affordable_moves(computer_energy))
        print(f"You chose {player_move}. The computer chose {computer_move}.")

        player_energy = min(MAX_ENERGY, player_energy - ATTACKS[player_move]["energy_cost"])
        computer_energy = min(MAX_ENERGY, computer_energy - ATTACKS[computer_move]["energy_cost"])

        player_wins = computer_move in ATTACKS[player_move]["beats"]
        computer_wins = player_move in ATTACKS[computer_move]["beats"]

        if player_wins and computer_wins:
            print("You both land a hit!")
            computer_health -= hit("You", player_move)
            player_health -= hit("Computer", computer_move)
        elif player_wins:
            damage = hit("You", player_move)
            computer_health -= damage
            print(f"Your {player_move} wins! " + (f"The computer takes {damage} damage." if damage else "You block the attack."))
        elif computer_wins:
            damage = hit("Computer", computer_move)
            player_health -= damage
            print(f"The computer's {computer_move} wins! " + (f"You take {damage} damage." if damage else "It blocks your attack."))
        else:
            print("Nobody lands a hit.")

        round_number += 1

    print()
    print(f"Final: You {max(0, player_health)} HP | Computer {max(0, computer_health)} HP")
    if player_health <= 0 and computer_health <= 0:
        print(f"Double knockout! It's a draw. You get your ${bid_amount} back.")
        player.money += bid_amount
    elif computer_health <= 0:
        winnings = bid_amount * WIN_MULTIPLIER
        player.money += winnings
        print(f"You won the battle and ${winnings}!")
    else:
        print(f"You lost the battle and your ${bid_amount} bid.")

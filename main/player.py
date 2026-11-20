#The most essential things in the game will be defined here.
import enum

class WorkState(enum.Enum):
    DONE = 1
    READY = 2
class Player:
    def __init__ (self, money, inventory, health, energy, happiness, work_state, last_work_time, last_hunted_time, hunger, luck, intelligence, perception, endurance, dexterity):
        self.money = money
        self.inventory = inventory
        self.health = health
        self.energy = energy
        self.happiness = happiness
        self.last_work_time = last_work_time
        self.bought_at = {}  # Dictionary to store the purchase time of each item
        self.default_work_state = work_state  # Default work state is READY
        self.last_hunted_time = last_hunted_time  # New attribute to track the last hunted time
        self.hunger = hunger
        self.intelligence = intelligence
        self.perception = perception
        self.endurance = endurance  # New attribute for endurance
        self.dexterity = dexterity  # New attribute for dexterity
        #special stats
        self.luck = luck
    def get_inventory(self):
        return self.inventory

    def set_inventory(self, inventory):
        self.inventory = inventory
    def get_money(self):
        return self.money

    def set_money(self, amount):
        self.money = amount

    def get_health(self):
        return self.health
    def set_health(self, health):
        self.health = health
    def get_energy(self):
        return self.energy
    def set_energy(self, energy):
        self.energy = energy
    def get_happiness(self):
        return self.happiness
    def set_happiness(self, happiness):
        self.happiness = happiness
    def get_work_state(self):
        return self.default_work_state
    def set_work_state(self, state):
        self.default_work_state = state
    def get_last_work_time(self):
        return self.last_work_time
    def set_last_work_time(self, timestamp):
        self.last_work_time = timestamp
    def get_hunger(self):
        return self.hunger
    def set_hunger(self, hunger):
        self.hunger = hunger
    def get_luck(self):
        return self.luck
    def set_luck(self, luck):
        self.luck = luck
    def get_intelligence(self):
        return self.intelligence
    def set_intelligence(self, intelligence):
        self.intelligence = intelligence
    def get_perception(self):
        return self.perception
    def set_perception(self, perception):
        self.perception = perception
    def get_endurance(self):
        return self.endurance
    def set_endurance(self, endurance):
        self.endurance = endurance

    def get_dexterity(self):
        return self.dexterity
    def set_dexterity(self, dexterity):
        self.dexterity = dexterity

    def get_last_hunted_time(self):
        return self.last_hunted_time
    def set_last_hunted_time(self, timestamp):
        self.last_hunted_time = timestamp

    def player_status(self):
        return {
            "money": self.money,
            "inventory": self.inventory,
            "health": self.health,
            "energy": self.energy,
            "happiness": self.happiness,
            "work_state": self.default_work_state,
            "last_work_time": self.last_work_time,
            "last_hunted_time": self.last_hunted_time,
            "hunger": self.hunger,
            "bought_at": self.bought_at,
            "luck": self.luck,
            "intelligence": self.intelligence,
            "perception": self.perception,
            "endurance": self.endurance,
            "dexterity": self.dexterity
        }

    def load_from_dict(self,data):
        # .get() gives a default value, so older save files without these fields still load
        self.money = data["money"]
        self.inventory = data["inventory"]
        self.health = data.get("health", 100)
        self.energy = data.get("energy", 100)
        self.happiness = data.get("happiness", 50)
        self.default_work_state = WorkState[data.get("work_state", "READY")]
        self.last_work_time = data.get("last_work_time", 0)
        self.hunger = data.get("hunger", 0)
        self.bought_at = data.get("bought_at", {})
        self.last_hunted_time = data.get("last_hunted_time", 0)
        self.luck = data.get("luck", 0)
    def to_dict(self):
        return {"money" : self.money, "inventory" : self.inventory, "health" : self.health, 
                "energy" : self.energy, "happiness" : self.happiness, "work_state" : self.default_work_state.name, 
                "last_work_time" : self.last_work_time, "hunger" : self.hunger, "bought_at" : self.bought_at,  "last_hunted_time" : self.last_hunted_time,
                "luck" : self.luck, "intelligence" : self.intelligence, "perception" : self.perception, "endurance" : self.endurance, "dexterity" : self.dexterity}




player = Player(100, {}, 100, 100, 50, WorkState.READY, 0, 0, 0, 0, 0, 0, 0, 0)  # Initialize the player with default values


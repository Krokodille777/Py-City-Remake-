#The most essential things in the game will be defined here.
import enum

class WorkState(enum.Enum):
    DONE = 1
    READY = 2
class Player:
    def __init__ (self, money, inventory, health, energy, happiness, work_state, last_work_time):
        self.money = money
        self.inventory = inventory
        self.health = health
        self.energy = energy
        self.happiness = happiness
        self.last_work_time = last_work_time
        self.default_work_state = work_state  # Default work state is READY
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

    def load_from_dict(self,data):
        self.money = data["money"]
        self.inventory = data["inventory"]
        self.health = data["health"]
        self.energy = data["energy"]
        self.happiness = data["happiness"]
        self.default_work_state = WorkState[data["work_state"]]

    def to_dict(self):
        return {"money" : self.money, "inventory" : self.inventory, "health" : self.health, "energy" : self.energy, "happiness" : self.happiness, "work_state" : self.default_work_state.name, "last_work_time" : self.last_work_time}



player = Player(100, {}, 100, 100, 50, WorkState.READY, 0)


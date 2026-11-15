#The most essential things in the game will be defined here.
class Player:
    def __init__ (self, money, inventory):
        self.money = money
        self.inventory = inventory
    def get_inventory(self):
        return self.inventory

    def set_inventory(self, inventory):
        self.inventory = inventory
    def get_money(self):
        return self.money

    def set_money(self, amount):
        self.money = amount

    def to_dict(self):
        return {"money" : self.money, "inventory" : self.inventory}

    def load_from_dict(self,data):
        self.money = data["money"]
        self.inventory = data["inventory"]



player = Player(100, {})


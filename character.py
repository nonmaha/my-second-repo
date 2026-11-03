import random

class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self, other):
        
        damage = int(self.attack_power * random.uniform(0.3, 0.9))
        
        other.hp -= damage
        print(f"{self.name} attacks {other.name} for {self.attack_power} damage!")

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name}: {self.hp} HP"

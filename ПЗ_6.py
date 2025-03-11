from abc import ABC, abstractmethod

class character(ABC):
    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def defend(self):
        pass

class warrior(character):
    def __init__(self, strength):
        self.strength = strength
    def attack(self):
        return f"Воин атакует с показателем {self.strength * 3}"

    def defend(self):
        return f"Воин защищается с показателем: {self.strength}"


class mage(character):
    def __init__(self, mana):
        self.mana = mana
    def attack(self):
        return f"Маг атакует с показателем: {self.mana * 4}"

    def defend(self):
        return f"Маг защищается с показателем: {self.mana / 2}"


class archer(character):
    def __init__(self, accuracy):
        self.accuracy = accuracy
    def attack(self):
        return f"Лучник стреляет с показателем: {self.accuracy}"

    def defend(self):
        return f"Лучник защищается с показателем: {self.accuracy/2}"

Warrior = warrior(strength=10)
Mage = mage(mana=20)
Archer = archer(accuracy=15)

print(Warrior.attack())
print(Warrior.defend())

print()

print(Mage.attack())
print(Mage.defend())

print()

print(Archer.attack())
print(Archer.defend())
from abc import ABC, abstractmethod


class character(ABC):
    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def defend(self):
        pass


class warrior(character):
    def attack(self):
        return f"Воин атакует с показателем: 10"

    def defend(self):
        return f"Воин защищается с показателем: 3"


class mage(character):
    def attack(self):
        return f"Маг атакует с показателем: 7"

    def defend(self):
        return f"Маг защищается с показателем: 4"


class archer(character):
    def attack(self):
        return f"Лучник стреляет с показателем: 8"

    def defend(self):
        return f"Лучник защищается с показателем: 10"

Warrior = warrior()
Mage = mage()
Archer = archer()

print(Warrior.attack())
print(Warrior.defend())

print()

print(Mage.attack())
print(Mage.defend())

print()

print(Archer.attack())
print(Archer.defend())
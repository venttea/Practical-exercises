'''
Задание №1

class Rival:
    def __init__(self):
        self._life = 3
    
    def get_live(self):
        return self._life
    
    def set_live(self, live):
        self._live = live
        
    def attack(self):
        print("Ouch!")
        self._life -=1
        
    def checkLife(self):
        if self._life <=0:
            print("You won!")
        else:
            print(self._life)
            
thanos = Rival()
magneto = Rival()

thanos.attack()
thanos.attack()
thanos.attack()
thanos.checkLife()

print()

magneto.attack()
magneto.attack()
magneto.attack()
magneto.checkLife()
'''


'''
Задание №3
'''

class SoyuzDocking:
    def __init__(self):
        self.distance = 500 #расстояние до станции
        self.speed = 50 #скорость корабля
        self. fuel = 100 #количество топлива
        
    def perform_burn(self, burn_amount):
        self.speed = max(self.speed - burn_amount,0)
        self.fuel = max(self.fuel - burn_amount,0)
        
    def update_distance(self):
        self.distance = max(self.distance - self.speed, 0)
        
    def has_docked(self):
        return self.distance <= 0
        
docking_sequence = SoyuzDocking()

while not docking_sequence.has_docked():
    print(f"Расстояние до станции Салют-7: {docking_sequence.distance} метров")
    print(f"Скорость: {docking_sequence.speed} метров в секунду")
    print(f"Топливо: {docking_sequence.fuel} килограмм")
    
    if docking_sequence.fuel <= 0:
        print("Милорд!! Топливо кончилось!!!")
        break
    
    if docking_sequence.distance <= 11:
        autopilot = input("До станции Салют-7 осталось меньше 11 метро. Включить автопилот? (Да/ Нет)")
        
        if autopilot.lower() == 'да':
            print("Автопилот включен")
        else:
            print("Ну ок, давай сам тогда")
        break
    
    burn_amount = input("Сколько топлива сжечь для снижения скорости?")
    burn_amount = int(burn_amount)
        
    docking_sequence.perform_burn(burn_amount)
    docking_sequence.distance()
        
if docking_sequence.distance <= 11 and docking_sequence.speed <=docking_sequence.distance:
    print("Стыковка подтверждена. Поздравляем экипаж!")
else:
    print("Ничо не получилось, блин-блинский :(")
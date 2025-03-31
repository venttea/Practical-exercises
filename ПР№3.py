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

print("Добро пожаловать в симуляцию стыковки Союз Т-6!")
print("Ваша миссия – стыковка со станцией Салют-7.")
print("Вы можете управлять скоростью космического корабля сжигая топливо.")
print("Каждая единица сожженного топлива замедляет космический корабль на 1 м/с.")
print("Удачи экипажу!\n")

class SoyuzDocking:
    def __init__(self):
        self.distance = 500 #расстояние до станции
        self.speed = 50 #скорость корабля
        self.fuel = 100 #количество топлива
        
    def perform_burn(self, burn_amount):
        self.speed = max(self.speed - burn_amount, 0)
        self.fuel = max(self.fuel - burn_amount, 0)
        
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
        autopilot = input("До станции Салют-7 осталось меньше 11 метро. Включить автопилот? (Да/ Нет): ")
        
        if autopilot.lower() == 'да':
            print("Автопилот включен")
            break
    
    burn_amount = input("Сколько топлива сжечь для снижения скорости: ")
    burn_amount = int(burn_amount)
        
    docking_sequence.perform_burn(burn_amount)
    docking_sequence.update_distance()
        
if docking_sequence.distance <= 11 and docking_sequence.speed <= docking_sequence.distance:
    print("Стыковка подтверждена. Поздравляем экипаж!")
else:
    print("Ничо не получилось, блин-блинский :(")
'''

'''Задание по вар
8 вар.

билет: место, фильм, зал; показать информацию YES
зал: номер, количество мест; добавить фильм, удалить фильм, показать информацию МЕТОДЫ ДОДЕЛАТЬ
кино: название, жанр, длительность, режиссер, год выпуска; показать информацию YES
посетитель: фамиия, имя, возраст; показать информацию, проверка возраста YES
бронирование: фильм, зал, место, время; показать информацию YES

class ticket:
    def __init__(self, seat, movie, hall):
        self._seat = seat
        self._movie = movie
        self._hall = hall

    def get_seat(self):
        return self._seat
    def set_seat(self, seat):
        self._seat = seat

    def get_movie(self):
        return self._movie
    def set_movie(self, movie):
        self._movie = movie

    def get_hall(self):
        return self._hall
    def set_hall(self, hall):
        self._hall = hall

    def show_info_ticket(self):
        return f"\nМесто: {self._seat} \nЗал: {self._hall.get_number()} \nКино: {self._movie.show_info_movies()}"

class hall:
    def __init__(self, number, amount):
        self._number = number
        self._amount = amount
        self._movies_showing = []

    def get_number(self):
        return self._number
    def set_number(self, number):
        self._number = number

    def get_amount(self):
        return self._amount
    def set_amount(self, amount):
        self._amount = amount

    def add_movies(self, movie):
        if movie not in self._movies_showing:
            self._movies_showing.append(movie)

    def delete_movies(self, movie):
        if movie in self._movies_showing:
            self._movies_showing.remove(movie)

    def show_info_hall(self):
        return f"\nНомер зала: {self._number} \nВместительность зала: {self._amount}"
    
    def what_movies(self):
        return [movie.get_name() for movie in self._movies_showing]

class movie:
    def __init__(self, name, genre, duration, rating, director, release):
        self._name = name
        self._genre = genre
        self._duration = duration
        self._rating = rating
        self._director = director
        self._release = release
    
    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name

    def get_genre(self):
        return self._genre
    def set_genre(self, genre):
        self._genre = genre

    def get_duration(self):
        return self._duration
    def set_duration(self, duration):
        self._duration = duration

    def get_rating(self):
        return self._rating
    def set_rating(self, rating):
        self._rating = rating

    def get_director(self):
        return self._director
    def set_director(self, director):
        self._director = director

    def get_release(self):
        return self._release
    def set_release(self, release):
        self._release = release

    def show_info_movies(self):
        return f"\nНазвание: '{self._name}' ({self._release}) \nЖанр: {self._genre} \nРежиссер: {self._director} \nПродолжительность: {self._duration} минут \nРейтинг: {self._rating}"
    
    def is_movie_long(self):
        if self._duration > 120:
            return ("ДА")
        else:
            return ("НЕТ")

    def update_rating(self, new_rating):
        if 1 <= new_rating <= 10:
            self.set_rating(new_rating)
            return True
        return False

class visitor:
    def __init__(self, surname, name, age):
        self._surname = surname
        self._name = name
        self._age = age

    def get_surname(self):
        return self._surname
    def set_surname(self, surname):
        self._surname = surname

    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age
    def set_age(self, age):
        self._age = age

    def show_info_visitor(self): # Показ информации о человеке
        return f"\nФамилия: {self._surname} \nИмя: {self._name} \nВозраст: {self._age} лет"

    def is_adult(self):
        if self._age > 18:
            return ("ДА")
        else:
            return ("НЕТ")

class booking(ticket):
    def __init__(self, seat, movie, hall, time):
        super().__init__(seat, movie, hall)
        self._time = time

    def get_time(self):
        return self._time
    def set_time(self, time):
        self._time = time

    def show_info_booking(self): # Показ информации о бронировании
        base = super().show_info_ticket()
        return f"{base} \nВремя бронирования: {self._time}"
    
movie1 = movie("Майор Гром: Игра", "боевик, приключения", 168, 7.5, "Олег Трофим", 2024)
movie2 = movie("Корпорация монстров", "мультфильм, фэнтези, комедия, приключения, семейный", 92, 8.1, "Пит Доктер", 2001)
movie3 = movie("Гадкий я 4", "мультфильм, фантастика, комедия, криминал, приключения, семейный", 94, 6.5, "Крис Рено", 2024)

hall1 = hall(1, 40)
hall2 = hall(2, 25)

hall1.add_movies(movie1)
hall1.add_movies(movie2)
hall2.add_movies(movie1)
hall2.add_movies(movie2)
hall2.add_movies(movie3)

visitor1 = visitor("Hayes", "Nora", 22)
visitor2 = visitor("Harris", "Alice", 14)
visitor3 = visitor("Martinez", "Chris", 37)

ticket1 = ticket(12, movie2, hall2)
ticket2 = ticket(15, movie1, hall1)

booking1 = booking(12, movie2, hall2, "12:30")
booking2 = booking(15, movie1, hall1, "21:00")

print("\nИНФОРМАЦИЯ О КИНО")
print(movie1.show_info_movies())
print(movie2.show_info_movies())
print(movie3.show_info_movies())

print("\nИНФОРМАЦИЯ О ЗАЛАХ")
print(hall1.show_info_hall())
print(hall2.show_info_hall())

print("\nИНФОРМАЦИЯ О ПОСЕТИТЕЛЯХ")
print(visitor1.show_info_visitor())
print(visitor2.show_info_visitor())
print(visitor3.show_info_visitor())

print("\nИНФОРМАЦИЯ О БИЛЕТАХ")
print(ticket1.show_info_ticket())
print(ticket2.show_info_ticket())

print("\nИНФОРМАЦИЯ О БРОНИРОВАНИИ")
print(booking1.show_info_booking())
print(booking2.show_info_booking())

print("\nПРОВЕРКА РАБОТЫ МЕТОДА 'what_movies'")
print(f"Кино в первом зале:{hall1.what_movies()}")
print(f"Кино во втором зале:{hall2.what_movies()}")

print("\nПРОВЕРКА РАБОТЫ МЕТОДА 'is_movie_long'")
print(f"Фильм '{movie1.get_name()}' идет более двух часов?"+ f" Ответ: {movie1.is_movie_long()}")
print(f"Фильм '{movie2.get_name()}' идет более двух часов?"+ f" Ответ: {movie2.is_movie_long()}")
print(f"Фильм '{movie3.get_name()}' идет более двух часов?" + f" Ответ: {movie3.is_movie_long()}")

print("\nПРОВЕРКА РАБОТЫ МЕТОДА 'update_rating'")
rat1 = float(input(f"Введите рейтинг для фильма {movie1.get_name()} (от 1 до 10): "))
print(f"\nРейтинг фильма '{movie1.get_name()}' - {movie1._rating}")
if movie1.update_rating(rat1):
    print(f"Рейтинг фильма '{movie1.get_name()}' успешно обновлен!!")
else:
    print(f"ОШИБКА: Рейтинг фильма '{movie1.get_name()}' должен быть от 1 до 10")
print(f"Актуальный рейтинг фильма '{movie1.get_name()}' - {movie1._rating}")

rat2 = float(input(f"\nВведите рейтинг для фильма {movie2.get_name()} (от 1 до 10): "))
print(f"\nРейтинг фильма '{movie2.get_name()}' - {movie2._rating}")
if movie2.update_rating(rat2):
    print(f"Рейтинг {movie2.get_name()} успешно обновлен!!")
else:
    print(f"ОШИБКА: Рейтинг фильма '{movie2.get_name()}' должен быть от 1 до 10")
print(f"Актуальный рейтинг фильма '{movie2.get_name()}' - {movie2._rating}")

rat3 = float(input(f"\nВведите рейтинг для фильма {movie3.get_name()} (от 1 до 10): "))
print(f"\nРейтинг фильма '{movie3.get_name()}' - {movie3._rating}")
if movie3.update_rating(rat3):
    print(f"Рейтинг {movie3.get_name()} успешно обновлен!!")
else:
    print(f"ОШИБКА: Рейтинг фильма '{movie3.get_name()}' должен быть от 1 до 10")
print(f"Актуальный рейтинг фильма '{movie3.get_name()}' - {movie3._rating}")

print("\nПРОВЕРКА РАБОТЫ МЕТОДА 'delete_movies'")
print(f"Список фильмов в зале {hall2.get_number()}: {hall2.what_movies()}")
hall2.delete_movies(movie1)
print(f"Обновленный список фильмов в зале {hall2.get_number()}: {hall2.what_movies()}")

print("\nПРОВЕРКА РАБОТЫ МЕТОДА 'is_adult'")
print(f"{visitor1._surname} {visitor1._name} совершеннолетний (-яя)?" + f" Ответ: {visitor1.is_adult()}")
print(f"{visitor2._surname} {visitor2._name} совершеннолетний (-яя)?" + f" Ответ: {visitor2.is_adult()}")
print(f"{visitor3._surname} {visitor3._name} совершеннолетний (-яя)?" + f" Ответ: {visitor3.is_adult()}")
'''

'''
print("Добро пожаловать в симуляцию стыковки Союз Т-6!")
print("Ваша миссия – стыковка со станцией Салют-7.")
print("Вы можете управлять скоростью космического корабля сжигая топливо.")
print("Каждая единица сожженного топлива замедляет космический корабль на 1 м/с.")
print("Удачи экипажу!\n")

class SoyuzDocking:
    def __init__(self):
        self.distance = 500  # расстояние до станции
        self.speed = 50  # скорость корабля
        self.fuel = 100  # количество топлива

    def perform_burn(self, burn_amount):
        if burn_amount > self.fuel:
            print("Топлива не так много, чтоб вот таким заниматься придумал тоже")
            return False
        self.speed = max(self.speed - burn_amount, 0)
        self.fuel = max(self.fuel - burn_amount, 0)
        return True

    def update_distance(self):
        self.distance = max(self.distance - self.speed, 0)

    def has_docked(self):
        return self.distance <= 0

    def display_status(self):
        print(f"Расстояние до станции Салют-7: {self.distance} метров")
        print(f"Скорость: {self.speed} метров в секунду")
        print(f"Топливо: {self.fuel} килограмм")

    def enable_autopilot(self):
        print("Автопилот включен. Стыковка завершена.")
        self.distance = 0
        self.speed = 0

    def hand_docking_check(self):
        if self.distance <= 11 and self.speed <= self.distance:
            print("Стыковка подтверждена. Поздравляем экипаж!!")
        else:
            print("Ничо не получилось, блин-блинский")

# Основной цикл программы
docking_sequence = SoyuzDocking()

while not docking_sequence.has_docked():
    docking_sequence.display_status()

    if docking_sequence.fuel <= 0:
        print("Милорд!! Топливо кончилось!!!")
        break

    if docking_sequence.distance <= 11:
        autopilot = input("До станции Салют-7 осталось меньше 11 метров. Включить автопилот? (Да/Нет): ").lower()
        if autopilot == 'да':
            docking_sequence.enable_autopilot()
            break
        else:
            print("Ну нет так нет, давай сам")
            break

    try:
        burn_amount = int(input("Сколько топлива сжечь для снижения скорости: "))
        if burn_amount < 0:
            print("Количество топлива не может быть отрицательным, шутишь что ли")
            continue
        if docking_sequence.perform_burn(burn_amount):
            docking_sequence.update_distance()
    except ValueError:
        print("Пожалуйста, ну введи ты нормальное число, не до шуток")

docking_sequence.hand_docking_check()
'''
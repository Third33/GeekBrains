# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
# сообщение и завершать скрипт.
from itertools import cycle
from time import sleep
import check_input


class TrafficLight:
    __colors = {7: '\033[31m Red', 2: '\033[33m Yellow', 5: '\033[32m Green'}

    def __init__(self):
        self.__colors = self.__colors

    def running(self):
        sleep(0.5)
        for i in self.__colors:
            print(f'{self.__colors[i]} = {i} sek')
            self.load(i)

    def load(self, sek):  # Я не уверен, что функцию стоит запихивать в класс, но пусть будет
        lo_sym = cycle(['#' * el for el in range(sek + 1)])
        sleep(0.5)
        for i in range(sek + 1):
            print(f'[{next(lo_sym)}', end=f'{"." * (sek - i)}]')
            print(f' {sek - i} sek', end='')
            sleep(1)
            print('\r', end='')
        print()


def exe_1():
    tr_light = TrafficLight()
    tr_light.running()
    print('\033[0m')


# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длинаширинамасса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна.
# Проверить работу метода.
#
# Например: 20м*5000м*25кг*5см = 12500 т

class Road:
    weigth = 25

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def make_road(self, mass):
        return int((mass * self.weigth * self._length * self._width) / 1000)


def exe_2():
    road = Road(5000, 20)
    print(f'{road.make_road(5)} tonn')
    print(f'{road._length} length')
    print(f'{road._width} width')


# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и
# премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В
# классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (
# get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def income(self):
        return sum(self._income.values())


def exe_3():
    worker_1 = Position('Anton', 'Fedorov', 'Java/Groovy Developer', 1000, 500)
    worker_2 = Position('Petya', 'Petrov', 'Cleaner', 100000, 5000)
    print(worker_1.get_full_name())
    print(worker_1.position)
    print(worker_1.income(), '$')
    print()
    print(worker_2.get_full_name())
    print(worker_2.position)
    print(worker_2.income(), '$')


# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
# булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(fr'{self.name} rides. Speed is {self.speed} km\h.')

    def stop(self):
        self.speed = 0
        print(fr'{self.name} stops. Speed is {self.speed} km\h.')

    def turn(self, direction):
        print(f'{self.name} is turn to {direction}')

    def show_speed(self):  # Я специально не стал переопределять метод для WorkCar & TownCar классов, потому что это
        # можно сделать здесь, так нельзя? И если нельзя, напишите пожалуйста мне в комментарии к дз почему.
        if self.speed >= 40 and self.name == 'GarbageCar':
            print(fr'Warning! Speed limit {self.speed} km\h for {self.name}')
        elif self.speed >= 60 and self.name == 'VAZ-2107':
            print(fr'Warning! Speed limit {self.speed} km\h for {self.name}')
        else:
            print(fr'{self.name} speed {self.speed} km\h')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


def exe_4():
    town_car = TownCar(60, 'black', 'VAZ-2107', False)
    sport_car = SportCar(120, 'red', 'Ferrari', False)
    work_car = WorkCar(50, 'blue', 'GarbageCar', False)
    police_car = PoliceCar(240, 'white', 'Bicycle', True)

    town_car.go(), town_car.turn('right'), town_car.show_speed(), town_car.stop()
    print()
    sport_car.go(), sport_car.turn('forward'), sport_car.show_speed(), sport_car.stop()
    print()
    work_car.go(), work_car.turn('right'), work_car.show_speed(), work_car.stop()
    print()
    police_car.go(), print(f'Color is: {police_car.color}'), police_car.show_speed(), police_car.stop()


# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод
# draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из
# классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Start {self.title} draw')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Start {self.title} draw')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Start {self.title} draw')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Start {self.title} draw')


def exe_5():
    stationery = Stationery('Stationery')
    pen = Pen('Pen')
    pencil = Pencil('Pencil')
    handle = Handle('Handle')

    pen.draw()
    pencil.draw()
    handle.draw()
    stationery.draw()


def refresh():
    print('Выберите задание и его решение')
    for i in range(1, 6):
        print(f'Задание {i}. Введите: {i}')


menu = {1: exe_1,
        2: exe_2,
        3: exe_3,
        4: exe_4,
        5: exe_5,
        }

while True:
    refresh()
    number_user = check_input.user(input('Выберите задание или введите "q", чтобы выйти: '))
    if number_user in menu:
        # print(list_exe[number_user])
        print()
        x = menu[number_user]
        x()
        input('\nНажмите Enter, чтобы продолжить ')

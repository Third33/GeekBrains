# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором classmethod, должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных
# данных.
from Exercise import check_input


def exe_1():
    class Date(object):
        @classmethod
        def from_string(cls, date_string):
            day, month, year = map(int, date_string.split('-'))
            if Date.is_date_valid(day, month, year):
                print(f'День: {day}|Месяц: {month}|Год: {year}')
            else:
                print('Data is not valid')

        @staticmethod
        def is_date_valid(day, month, year):
            return day <= 31 and month <= 12 and year <= 3999

    Date.from_string('32-09-2012')
    Date.from_string('32-13-2012')
    Date.from_string('32-09-3000')
    Date.from_string('10-10-1010')


# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.


def exe_2():
    class MyZeroDivision(Exception):
        def init(self, text):
            self.txt = text

    a = int(input("Input positive integer: "))

    try:
        if a == 0:
            raise MyZeroDivision("You cant / 0!")
        else:
            print(int(100 / a))
    except ValueError:
        print("Error type of value!")
    except MyZeroDivision as mr:
        print(mr)


# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка. Примечание: длина списка не фиксирована.
# Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например,
# команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
#
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
# только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и
# отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.


def exe_3():
    class TextError(Exception):
        def __init__(self, text):
            self.txt = text

    array = []
    my_list = ''
    while True:
        x = input("Input any words or 'q' to exit: ")
        if x == 'q':
            print(array)
            break
        for i in x:
            try:
                if i.isdigit():
                    my_list = my_list + str(i)
                else:
                    raise TextError("No words")
            except ValueError:
                print(TextError("No words!"))
            except TextError as te:
                print(te)
        array.append(int(my_list))


# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер,
# ксерокс). В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать
# параметры, уникальные для каждого типа оргтехники.

def exe_4():
    class StoreHouse:
        def __init__(self):
            self.store = {}

        def create_item(self):
            item_list = {}
            i = 0
            while True:
                user_input = input('Choose item ("printer", "scaner", "herox") or "q" to stop: ')
                if user_input == 'q':
                    break
                if user_input in ['printer', 'scaner', 'herox', 'Printer', 'Scaner', 'Herox']:
                    try:
                        name = input(f'Enter {user_input} name: ')
                        cost = int(input(f'Enter {user_input} cost: '))
                        quantity = int(input(f'Enter {user_input} quantity: '))
                        unicnum = input(f'Enter unic {user_input} number: ')
                        if user_input == 'printer':
                            a = Printer(name, cost, quantity, unicnum)
                            i += 1
                            item_list[f'№{i}'] = a.tech
                        elif user_input == 'scaner':
                            a = Scaner(name, cost, quantity, unicnum)
                            i += 1
                            item_list[f'№{i}'] = a.tech
                        elif user_input == 'herox':
                            a = Herox(name, cost, quantity, unicnum)
                            i += 1
                            item_list[f'№{i}'] = a.tech
                    except:
                        print('Wrong input!')
                        continue
                else:
                    print('Wrong input')
                    continue
            return item_list

        def moving_item(self, item):
            office = input('Choose office (Moscow, St.Peterburg): ')
            self.store[office] = item
            return self.store

    class Orgtech:
        def __init__(self, model, cost, quantity):
            self.tech = {'Model': model, 'Cost': cost, 'Quantity': quantity}

    class Printer(Orgtech):
        def __init__(self, model, cost, quantity, pr_num):
            super().__init__(model, cost, quantity)
            self.tech['Unic_Num'] = pr_num

    class Scaner(Orgtech):
        def __init__(self, model, cost, quantity, sc_num):
            super().__init__(model, cost, quantity)
            self.tech['Unic_Num'] = sc_num

    class Herox(Orgtech):
        def __init__(self, model, cost, quantity, hr_num):
            super().__init__(model, cost, quantity)
            self.tech['Unic_Num'] = hr_num

    sh = StoreHouse()
    sh.moving_item(sh.create_item())
    for key, value in sh.store.items():
        print(key, value)


# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные
# числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

def exe_5():
    class Complex:
        def __init__(self, real, imag):
            self.real = real
            self.imag = imag

        def __str__(self):
            sign = '+' if self.imag >= 0 else ''
            return '{}{}{}i'.format(self.real, sign, self.imag)

        def __add__(self, other):
            real = self.real + other.real
            imag = self.imag + other.imag
            return Complex(real, imag)

        def __sub__(self, other):
            real = self.real - other.real
            imag = self.imag - other.imag
            return Complex(real, imag)

        def __mul__(self, other):
            real = self.real * other.real - self.imag * other.imag
            imag = self.imag * other.real + self.real * other.imag
            return Complex(real, imag)

        def __abs__(self):
            return (self.real ** 2 + self.imag ** 2) ** 0.5

    print(Complex(1, 2) + Complex(3, 4))
    print(Complex(1, 2) * Complex(3, 4))
    print(Complex(1, 2) - Complex(3, 4))
    print(abs(Complex(3, 4)))


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

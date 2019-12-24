# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.


def exe_var():
    a = 'Hello'
    b = 10
    c = 3.3
    d = True

    print(f'{type(a)} = {a},\n {type(b)} = {b},\n {type(c)} = {c},\n {type(d)} = {d}\n')

    user_input0 = str(input('Input string: '))
    user_input1 = int(input('Input integrity: '))

    print(f'Your int = {user_input1} = {type(user_input1)},\nYour str = {user_input0} = {type(user_input0)}')


# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.


def exe_time_1():  # Дефолтное решение
    time_ = int(input('Input time in seconds: '))
    print(f"Time = {time_ // 3600}:{(time_ // 60) % 60}:{time_ % 60}")


def exe_time_2():  # Решение через цикл
    time_ = int(input('Input time in seconds: '))
    hours = 0
    minutes = 0
    seconds = 0

    while time_ > 0:
        seconds += 1
        time_ -= 1
        if seconds == 60:
            seconds = seconds - 60
            minutes += 1
            if minutes == 60:
                minutes = minutes - 60
                hours += 1

    print(f'{hours}:{minutes}:{seconds}')


def exe_time_3():  # Решение через импорт библиотеки
    import datetime
    print(str(datetime.timedelta(seconds=int(input('Input time in seconds: ')))))


# 3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.


def exe_sum_1():
    n = int(input('Input number: '))
    print(n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n)))


def exe_sum_2():  # number = число и кол-во сложений
    number = int(input('Input number: '))
    i = 1
    sum_str = ''
    sum_int = 0
    while i <= number:
        i += 1
        sum_str += str(number)
        sum_int = sum_int + int(sum_str)
    print(sum_int)


#  4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.


def exe_max_1():  # Решение через цикл
    number = int(input('Input int number: '))
    result = 0
    while number >= 1:
        const = number % 10
        number //= 10
        if const > result:
            result = const
    print(result)


def exe_max_2():  # Решение через функцию max :)
    print(max([int(s) for s in input('Input integrity number: ')]))


#  5. Запросите у пользователя значения выручки и издержек фирмы.
#  Определите, с каким финансовым результатом работает фирма
#  (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
#  Выведите соответствующее сообщение.
#  Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
#  Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.


def exe_company_1():
    earnings = float(input('Input earnings: '))
    costs = float(input('Input costs: '))
    if earnings > costs:
        print(f'Your company income: {(earnings - costs):.2f}$\nYour company ratio: {earnings / costs:.2f} to 1')
        workers = int(input('Input how much workers do u have: '))
        print(f'Workers gain company: {(earnings - costs) / workers:.2f}$')
    elif earnings < costs:
        print(f'Your company consumption: {(costs - earnings):.2f}')


#  6. Спортсмен занимается ежедневными пробежками.
#  В первый день его результат составил a километров.
#  Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
#  Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
#  Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

def exe_run_1():
    first_day = int(input('Input first day result: '))
    target_km = int(input('Input target km: '))
    day = 1
    while first_day < target_km:
        first_day += (first_day / 100) * 10
        day += 1
    print(f'Day number: {day}, Future result: {first_day:.2f} km')


def sep():
    print('+' * 30)


def refresh():
    print('Выберите задание и его решение')
    sep()
    print('Задание 1. Кол-во решений: 1. Введите: 11')
    sep()
    print('Задание 2. Кол-во решений: 3. Введите: 21 или 22 или 23')
    sep()
    print('Задание 3. Кол-во решений: 2. Введите: 31 или 32')
    sep()
    print('Задание 4. Кол-во решений: 2. Введите: 41 или 42')
    sep()
    print('Задание 5. Кол-во решений: 1. Введите: 51')
    sep()
    print('Задание 6. Кол-во решений: 1. Введите: 61\n')


# Начало

menu = {11: exe_var,
        21: exe_time_1,
        22: exe_time_2,
        23: exe_time_3,
        31: exe_sum_1,
        32: exe_sum_2,
        41: exe_max_1,
        42: exe_max_2,
        51: exe_company_1,
        61: exe_run_1, }

number_user = 1

while number_user != 0:
    refresh()
    number_user = int(input('Выберите задание или введите "0", чтобы выйти: '))
    if number_user == 0:
        break
    if number_user in menu:  # Проверку на строки не осилил
        x = menu[number_user]
        x()
        input('Нажмите Enter, чтобы продолжить ')

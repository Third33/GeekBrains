# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def exe_1(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'No / 0'
    except ValueError:
        return 'No value'


def exe_1_use():
    print(exe_1((int(input('Enter first number: '))), (int(input('Enter second number: ')))))


# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def exe_2(**kwargs):
    return list(kwargs.values())


def exe_2_use():
    print(exe_2(name=input('Enter name: '),
                s_name=input('Enter second name: '),
                b_date=input('Enter birth day: '),
                l_town=input('Enter live town: '),
                email=input('Enter email: '),
                tel=input('Enter tel number: ')))


# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def exe_3(a, b, c):
    z = [a, b, c]
    z.remove(min(a, b, c))
    return sum(z)


def exe_3_use():
    print(exe_3(4, 1, 9))


# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.


def exe_4(x, y):
    return 1 / x ** abs(y)


def exe_4_use():
    print(exe_4(2, -2))


def exe_41(x, y):
    for i in range(abs(y - 1)):
        x *= x
    return 1 / x


def exe_41_use():
    print(exe_41(2, -2))


# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме
# и после этого завершить программу.


def exe_5():
    res = 0
    while True:
        numbers = input('Enter list of number or * to exit: ').split()
        for i in numbers:
            try:
                if i == '*':
                    print(f'Sum is {res}. Exit')
                    return
                else:
                    res += int(i)
            except ValueError:
                print('Enter number or *')
        print(f'Sum is {res}')


# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
# и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().


def exe_6(text):
    ls = []
    for i in range(len(text)):
        ls.append(text[i][0:1].title() + text[i][1:])
    return ' '.join(ls)


def exe_6_use():
    print(exe_6(input('Input text: ').split()))


def sep():
    print('+' * 30)


def refresh():
    print('Выберите задание и его решение')
    sep()
    print('Задание 1. Введите: 1')
    sep()
    print('Задание 2. Введите: 2')
    sep()
    print('Задание 3. Введите: 3')
    sep()
    print('Задание 4. Введите: 4 или 41 (2 решения)')
    sep()
    print('Задание 5. Введите: 5')
    sep()
    print('Задание 6. Введите: 6\n')


# Начало


menu = {1: exe_1_use,
        2: exe_2_use,
        3: exe_3_use,
        4: exe_4_use,
        41: exe_41_use,
        5: exe_5,
        6: exe_6_use,
        }

number_user = 1

while number_user != 0:
    refresh()
    number_user = int(input('Выберите задание или введите "0", чтобы выйти: '))
    if number_user == 0:
        break
    if number_user in menu:
        x = menu[number_user]
        x()
        input('Нажмите Enter, чтобы продолжить ')

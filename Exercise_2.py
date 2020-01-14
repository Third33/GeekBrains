# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.


def exe_1():
    my_list = ['Hello', 69.9, 100, True, [1, 2, 3]]
    for i in my_list:
        print(i, type(i))


# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().


def exe_2():
    l = list(input('Enter anything: '))
    for i in range(1, len(l), 2):
        l[i - 1], l[i] = l[i], l[i - 1]
    print(' '.join([str(i) for i in l]))


# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.


def exe_3():
    n = int(input("Enter month number: "))
    if 12 >= n >= 1:
        d_month = dict.fromkeys([1, 2], 'Winter')
        d_month.update(d_month.fromkeys([3, 4, 5], 'Spring'))
        d_month.update(d_month.fromkeys([6, 7, 8], 'Summer'))
        d_month.update(d_month.fromkeys([9, 10, 11], 'Autumn'))
        d_month.update(d_month.fromkeys([12], 'Winter'))
        l_month = list(d_month.values())
        for i, nm in enumerate(l_month):
            if i == n - 1:
                print(f'List month: {l_month[i]}')
                break
        print(f'Dict month: {d_month[n]}')
    else:
        print('Enter number 1 - 12')


# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.


def exe_4():
    list_words = list(input('Enter words: ').split())
    for i, value in enumerate(list_words, 1):
        value = value[:10] if len(value) > 10 else value
        print(f'{i}: {value}')


# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

def exe_5():
    num = int(input("Enter number: "))
    ls = [3, 2, 3, 5, 6, 9]
    for el in ls:
        if ls.count(num) > 0:
            ls.insert(ls.index(num) + ls.count(num), num)
            break
        else:
            if num > el:
                ls.insert(ls.index(el), num)
                break
            elif num < ls[len(ls) - 1]:
                ls.append(num)
    print(ls)


# 6. *Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно,
# т.е. запрашивать все данные у пользователя.

# Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик,
# например список названий товаров.


def exe_6():
    gs = []
    num = 0
    while input("Add product? Enter y/n: ") == 'y':
        num += 1
        param = {}
        while input("Add product parameters? Enter y/n: ") == 'y':
            p_key = input("Enter feature product: ")
            p_value = input("Enter feature value product: ")
            param[p_key] = p_value
        gs.append(tuple([num, param]))
    print(gs)
    stat = {}
    for i in gs:
        for p_key, p_value in i[1].items():
            if p_key in stat:
                stat[p_key].append(p_value)
            else:
                stat[p_key] = [p_value]
    print(stat)


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
    print('Задание 4. Введите: 4')
    sep()
    print('Задание 5. Введите: 5')
    sep()
    print('Задание 6. Введите: 6\n')


# Начало


menu = {1: exe_1,
        2: exe_2,
        3: exe_3,
        4: exe_4,
        5: exe_5,
        6: exe_6,
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

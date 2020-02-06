from functools import reduce
from itertools import cycle, count
from Exercise import check_input as check

list_exe = {1: '',
            2: '\n2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше '
               'предыдущего элемента.\n',
            3: '\n3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в '
               'одну строку.\n',
            4: '\n4. Представлен список чисел. \nОпределить элементы списка, не имеющие повторений. \nСформировать '
               'итоговый массив чисел, соответствующих требованию. \nЭлементы вывести в порядке их следования в '
               'исходном списке. \nДля выполнения задания обязательно использовать генератор. \n',
            5: '\n5. Реализовать формирование списка, используя функцию range() и возможности генератора. \nВ список '
               'должны войти четные числа от 100 до 1000 (включая границы). \nНеобходимо получить результат вычисления '
               'произведения всех элементов списка.\n',
            6: '\n6. Реализовать два небольших скрипта:\n а) бесконечный итератор, генерирующий целые числа, начиная с '
               'указанного,\n б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее. '
               '\nПодсказка: использовать функцию count() и cycle() модуля itertools.\n',
            7: '\n7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. '
               '\nПри вызове функции должен создаваться объект-генератор. \nФункция должна вызываться следующим '
               'образом: '
               'for el in fact_gen(). \nФункция отвечает за получение факториала числа, а в цикле необходимо выводить '
               'только первые 15 чисел.\n '
            }


def exe_2(my_list):
    return [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i - 1]]


def exe_2_use():
    array = check.gen_list(input('Enter range for array: '))
    print(array, exe_2(array), sep='\n')


def exe_3():
    min_ = check.user(input('Enter minimum range (20): '), True)
    max_ = check.user(input('Enter maximum range (240): '), True)
    print([el for el in range(min_, max_ + 1) if el % 20 == 0 or el % 21 == 0])


def exe_4():
    my_list = check.gen_list(input('Enter range for array: '))
    print(my_list, [el for el in my_list if my_list.count(el) == 1], sep='\n')


def exe_5():
    # Вывод получается слишком огромным, поэтому ограничил в 100 символов.
    min_ = check.user(input('Enter minimum range: '), True)
    max_ = check.user(input('Enter maximum range: '), True)
    print('\nВывод ограничен 100 символами\n', str(reduce(lambda s, i: s * i, [el for el in range(min_, max_ + 1, 2)]))[:100], sep='\n')


def exe_6():
    user_range = check.user(input('Enter count of str (Rec: 10): '), True)
    a = cycle(count())
    b = cycle([el for el in check.gen_list(input('Enter array range (Rec: 5): '))])
    for i in range(user_range):
        print(next(a), next(b))


def exe_7(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
        yield res


def exe_7_1():
    for el in exe_7(check.user(input('Enter count of factorial (Rec: 15): '), True)):
        print(el)


def sep():
    print('+' * 30)


def refresh():
    print('Выберите задание и его решение')
    sep()
    print('Задание 2. Введите: 2')
    sep()
    print('Задание 3. Введите: 3')
    sep()
    print('Задание 4. Введите: 4')
    sep()
    print('Задание 5. Введите: 5')
    sep()
    print('Задание 6. Введите: 6')
    sep()
    print('Задание 7. Введите: 7\n')


# Начало


menu = {2: exe_2_use,
        3: exe_3,
        4: exe_4,
        5: exe_5,
        6: exe_6,
        7: exe_7_1
        }


while True:
    refresh()
    number_user = check.user(input('Выберите задание или введите "q", чтобы выйти: '))
    if number_user in menu:
        print(list_exe[number_user])
        x = menu[number_user]
        x()
        input('\nНажмите Enter, чтобы продолжить ')

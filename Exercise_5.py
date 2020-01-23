import check_input
import re
import json


def exe_1():
    with open('text_1.txt', 'w+') as f:
        while True:
            a = input("Enter str: ")
            if not a:
                break
            f.write(f'{a}\n')


def exe_2():
    with open('text_2.txt', 'r') as f:
        print(f.read())
        f.seek(0, 0)
        print(f'Кол-во слов: {len(f.read().split())}')
        f.seek(0, 0)
        print(f'Кол-во строк: {len(f.read().splitlines())}')


def exe_3():
    dictionary = {}
    with open('text_3.txt', 'r') as f:
        for line in f:
            name, cash = line.split()
            dictionary[name] = float(cash)
        for key, value in dictionary.items():
            if value < 20000:
                print(f'Outsiders: {key} = {dictionary[key]}')
        print(f'Average cash is {sum(dictionary.values()) / len(dictionary):.2f}')


def exe_4():
    numbers = ["Один", "Два", "Три", "Четыре"]
    with open('text_4.txt', 'r') as f:
        print(f.read())
        f.seek(0, 0)
        my_file = open('text_4_new.txt', 'w+')
        for i, line in enumerate(f):
            str_line = line.split()
            my_file.write(line.replace(str_line[0], numbers[i]))
        my_file.close()
    with open('text_4_new.txt', 'r') as ft:
        print(ft.read())


def exe_5():
    with open('text_5.txt', 'w+') as f:
        num = check_input.gen_list(10)  # Используется генератор из библиотеки check_input
        f.writelines(' '.join(list(map(str, num))))
        f.seek(0, 0)
        print(f'Original list: {f.read()}')
        print(f'Sum numbers: {sum(num)}')


def check(text):
    try:
        first_list = ["".join(i for i in text if i.isdigit())]
        second_list = [int(i) for i in first_list]
        return second_list
    except:
        return [0]


def cw_reg(text):
    return list(map(int, re.findall(r'\d*\S[0-9]', text)))


def exe_6():
    my_list = {}
    with open('text_6.txt', 'r') as f:
        print(f.read())
        f.seek(0, 0)
        for line in f:
            name, lec, prac, lab = line.split()
            my_list[name] = sum(cw_reg(lec) + cw_reg(prac) + cw_reg(lab))
            # Для использования обычной функции, заменить cw_reg() на check()
        print(f'\nAll time for lesson - \n {my_list}')


def exe_7():
    my_list = []
    frm_list = {}

    with open('text_7.txt', 'r') as f:
        for line in f:
            name, form, cash, costs = line.split()
            frm_list[name] = int(cash) - int(costs)
        a_cash = [i for i in frm_list.values() if i > 0]
        avr_list = {'Average': int(sum(a_cash) / len(a_cash))}
        my_list.append(frm_list), my_list.append(avr_list)

    with open('text_7.json', 'w') as fl:
        json.dump(my_list, fl, indent=4, ensure_ascii=False)

    with open('text_7.json', 'r') as fq:
        print(fq.read())


# Начало


def refresh():
    print('Выберите задание и его решение')
    for i in range(1,8):
        print(f'Задание {i}. Введите: {i}')


list_exe = {1: '\n1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые '
               'пользователем.\n Об окончании ввода данных свидетельствует пустая строка.\n',
            2: '\n2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет '
               'количества строк, количества слов в каждой строке.\n',
            3: '\n3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их '
               'окладов\n. '
               'Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников\n. '
               '\nВыполнить подсчет средней величины дохода сотрудников\n.',
            4: '\n4. Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.\n '
               'При этом английские числительные должны заменяться на русские.\n '
               'Новый блок строк должен записываться в новый текстовый файл.\n',
            5: '\n5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных '
               'пробелами. \nПрограмма должна подсчитывать сумму чисел в файле и выводить ее на экран.\n',
            6: '\n6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и '
               'наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.\n Важно, '
               'чтобы для каждого предмета не обязательно были все типы занятий.\n Сформировать словарь, содержащий '
               'название предмета и общее количество занятий по нему.\n Вывести словарь на экран.\n',
            7: '\n7. Создать (не программно) текстовый файл, '
               'в котором каждая строка должна содержать данные о фирме:\n '
               'название, форма собственности, выручка, издержки. \n Необходимо построчно прочитать файл, вычислить '
               'прибыль каждой компании, а также среднюю прибыль. \n Если фирма получила убытки, в расчет средней '
               'прибыли ее не включать. \n Далее реализовать список. \n Он должен содержать словарь с фирмами и их '
               'прибылями, а также словарь со средней прибылью. \n Если фирма получила убытки, также добавить ее в '
               'словарь (со значением убытков). '

            }

menu = {1: exe_1,
        2: exe_2,
        3: exe_3,
        4: exe_4,
        5: exe_5,
        6: exe_6,
        7: exe_7,
        }

while True:
    refresh()
    number_user = check_input.user(input('Выберите задание или введите "q", чтобы выйти: '))
    if number_user in menu:
        print(list_exe[number_user])
        x = menu[number_user]
        x()
        input('\nНажмите Enter, чтобы продолжить ')

# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv
from Exercise import check_input as check

name, wrk_time, cash_hour, bonus = argv


def exe_1(wrk_time, cash_hour, bonus):
    if check.input_(wrk_time, cash_hour, bonus):
        wrk_time, cash_hour, bonus = check.input_(wrk_time, cash_hour, bonus)
        print(f'Your money is: {wrk_time * cash_hour + bonus}$')
    else:
        print('Only numbers')


exe_1(wrk_time, cash_hour, bonus)

# Command line: python3 Exercise_4.py 5 5 5

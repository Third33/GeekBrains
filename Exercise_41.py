# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv
import check_input as check


name, param_1, param_2, param_3 = argv


def exe_1(wrk_time, cash_hour, bonus):
    wrk_time, cash_hour, bonus = check.input_(wrk_time, cash_hour, bonus)
    return wrk_time * cash_hour + bonus


print(f'Your money is: {exe_1(param_1, param_2, param_3)}$')


# Command line: python3 Exercise_4.py 5 5 5

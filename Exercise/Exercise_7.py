# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен
# принимать данные (список списков) для формирования матрицы. Подсказка: матрица — система некоторых математических
# величин, расположенных в виде прямоугольной схемы. Примеры матриц вы найдете в методичке. Следующий шаг —
# реализовать перегрузку метода str() для вывода матрицы в привычном виде. Далее реализовать перегрузку метода add()
# для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая
# матрица. Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.
from abc import ABC, abstractmethod
from Exercise import check_input


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matrix]))

    def __add__(self, other):
        for i in range(len(self.matrix)):
            for j in range(len(other.matrix[0])):
                self.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(self.matrix)


def exe_1():
    mtx_1 = Matrix([[3, 33, 333],
                    [2, 22, 222],
                    [1, 11, 111]])
    mtx_2 = Matrix([[5, 55, 555],
                    [8, 78, 778],
                    [2, 22, 222]])

    print(mtx_1 + mtx_2)


# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
# проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и
# костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные
# числа: V и H, соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
# (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных. Реализовать общий
# подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для
# основных классов проекта, проверить на практике работу декоратора @property.


class Cloth(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def cost(self):
        pass


class Coat(Cloth):
    def __init__(self, size):
        super().__init__()
        self.size = size

    @property
    def cost(self):
        return self.size / 6.5 + 0.5


class Jacet(Cloth):
    def __init__(self, height):
        super().__init__()
        self.height = height

    @property
    def cost(self):
        return self.height * 2 + 0.3


def exe_2():
    coat = Coat(42)
    jac = Jacet(39)

    print(f'Размер пальто: {coat.size} Ткани на пальто: {coat.cost:.2f}m')
    print(f'Размер пиджака: {jac.height} Ткани на пиджак: {jac.cost:.2f}m')
    print(f'Общее кол-во на две вещи: {coat.cost + jac.cost:.2f}')


# 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе
# инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы методы
# перегрузки арифметических операторов: сложение (add()), вычитание (sub()), умножение (mul()), деление (truediv(
# )).Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не
# целочисленное) деление клеток, соответственно. В методе деления должно осуществляться округление значения до целого
# числа.

class Cell:
    def __init__(self, nuc):
        self.nuc = nuc

    def __str__(self):
        return str(f'Ячейка имеет {self.nuc} клеток')

    def __add__(self, other):
        return Cell(self.nuc + other.nuc)

    def __sub__(self, other):
        return Cell(self.nuc - other.nuc if (self.nuc - other.nuc) > 0 else print('Отрицательно!'))

    def __mul__(self, other):
        return Cell(int(self.nuc * other.nuc))

    def __truediv__(self, other):
        return Cell(round(self.nuc // other.nuc))

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.nuc / cells_in_row)):
            row += f'{"*" * cells_in_row} \n'
        print(f'{"=" * 10}')
        row += f'{"*" * (self.nuc % cells_in_row)}'
        return row


def exe_3():
    cells1 = Cell(50)
    cells2 = Cell(40)

    print(cells1)
    print(cells1 + cells2)
    print(cells1 - cells2)
    print(cells1 / cells2)
    print(cells1 * cells2)
    print(cells2.make_order(8))
    print(cells1.make_order(13))


def refresh():
    print('Выберите задание и его решение')
    for i in range(1, 4):
        print(f'Задание {i}. Введите: {i}')


menu = {1: exe_1,
        2: exe_2,
        3: exe_3,
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


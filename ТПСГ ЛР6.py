from prettytable import PrettyTable
import matplotlib.pyplot as plt

from ТПСГ_ЛР5.ЛР1 import LR1
from ТПСГ_ЛР5.ЛР2 import LR2
from ТПСГ_ЛР5.ЛР3 import LR3
from ТПСГ_ЛР5.ЛР4 import LR4


def Print_table(data1, data2, data3, data4):
    l1, l2, l3, l4 = len(list(set(data1))), len(list(set(data2))), len(list(set(data3))), len(list(set(data4)))
    table = PrettyTable()
    table.field_names = ["Какая работа", "Уникальные значения", "По скольки значениям построено"]
    table.add_row(['LR1', str(l1), str(len(data1))])
    table.add_row(['LR2', str(l2), str(len(data2))])
    table.add_row(['LR3', str(l3), str(len(data3))])
    table.add_row(['LR4', str(l4), str(len(data4))])
    # table.border = False
    # table.header = False
    return print(table)


def Count(mass):
    x, y = [], []
    for i in range(len(mass)):
        x.append(mass[i])
        y.append(i)
    return x, y


figure, axis = plt.subplots(2, 2, figsize=(15, 8))

data1 = LR1(7, 106, 1283, 6075, 500)

data2 = LR2(40, 5, 57, 45, 512, 500)

data3 = LR3('x**11+x**2+1', 2, '11111111100', 1)

data4 = LR4('x**4+x**3+1', 1, 1, '1100',
            'x**4+1', 1, 1, '1101',
            'x**6+x**1+1', 1, 1, '100111')

Print_table(data1, data2, data3, data4)
print(f"Последовательность 1:\n\t{data1}\n"
      f"Последовательность 2:\n\t{data2}\n"
      f"Последовательность 3:\n\t{data3}\n"
      f"Последовательность 4:\n\t{data4}\n")

x1, y1 = Count(data1)
axis[0, 0].scatter(y1, x1, color="black", s=5)
axis[0, 0].set_xlabel(r'$x$', fontsize=14)
axis[0, 0].set_ylabel(r'$y$', fontsize=14, rotation=0)

x2, y2 = Count(data2)
axis[0, 1].scatter(x2, y2, color="black", s=5)
axis[0, 1].set_xlabel(r'$x$', fontsize=14)
axis[0, 1].set_ylabel(r'$y$', fontsize=14, rotation=0)

x3, y3 = Count(data3)
axis[1, 0].scatter(x3, y3, color="black", s=5)
axis[1, 0].set_xlabel(r'$x$', fontsize=14)
axis[1, 0].set_ylabel(r'$y$', fontsize=14, rotation=0)

x4, y4 = Count(data4)
axis[1, 1].scatter(x4, y4, color="black", s=5)
axis[1, 1].set_xlabel(r'$x$', fontsize=14)
axis[1, 1].set_ylabel(r'$y$', fontsize=14, rotation=0)

figure.tight_layout(pad=5.0)
plt.show()
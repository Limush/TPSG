from ТПСГ_ЛР5.ЛР1 import LR1
from ТПСГ_ЛР5.ЛР2 import LR2
from ТПСГ_ЛР5.ЛР3 import LR3
from ТПСГ_ЛР5.ЛР4 import LR4

import matplotlib.pyplot as plt


figure, axis = plt.subplots(2, 2, figsize=(15, 8))

data1 = LR1(1, 106, 0, 500, 27)

data2 = LR2(2, 5, 1, 3, 6, 30)

data3 = LR3('x**7+x**4+1', 1, '1110001', 1)

data4 = LR4('x**4+x**3+1', 1, 1, '1100',
            'x**4+1', 1, 1, '1101',
            'x**6+x**1+1', 1, 1, '100111')
l1, l2, l3, l4 = len(list(set(data1))), len(list(set(data2))), len(list(set(data3))), len(list(set(data4)))
print(f"Уникальных 1 = {l1}\n"
      f"Уникальных 2 = {l2}\n"
      f"Уникальных 3 = {l3}\n"
      f"Уникальных 4 = {l4}\n"
      f"Вывожу 1 = {len(data1)}\n"
      f"Вывожу 2 = {len(data2)}\n"
      f"Вывожу 3 = {len(data3)}\n"
      f"Вывожу 4 = {len(data4)}\n"
      f"Последовательность 1:\n\t"
      f"{data1}\n"
      f"Последовательность 2:\n\t"
      f"{data2}\n"
      f"Последовательность 3:\n\t"
      f"{data3}\n"
      f"Последовательность 4:\n\t"
      f"{data4}\n")

axis[0, 0].hist(data1, bins=l1*5, color='skyblue', edgecolor='black')
axis[0, 1].hist(data2, bins=l2*5, color='skyblue', edgecolor='black')
axis[1, 0].hist(data3, bins=l3*5, color='skyblue', edgecolor='black')
axis[1, 1].hist(data4, bins=l4*10, color='skyblue', edgecolor='black')
plt.show()
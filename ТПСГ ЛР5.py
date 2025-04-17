from ТПСГ_ЛР5.ЛР1 import LR1
from ТПСГ_ЛР5.ЛР2 import LR2
from ТПСГ_ЛР5.ЛР3 import LR3
from ТПСГ_ЛР5.ЛР4 import LR4

import matplotlib.pyplot as plt


figure, axis = plt.subplots(2, 2, figsize=(15, 8))

data1 = sorted(LR1(1, 106, 0, 500, 19))

data2 = sorted(LR2(2, 5, 1, 3, 6, 10))

data3 = sorted(LR3('x**7+x**4+1', 1, '1110001', 1))

data4 = sorted(LR4('x**4+x**3+1', 1, 1, '1100',
                   'x**4+1', 1, 1, '1101',
                   'x**2+x**1+1', 1, 1, '11'))

axis[0, 0].hist(data1, bins=10, color='skyblue', edgecolor='black')
axis[0, 1].hist(data2, bins=10, color='skyblue', edgecolor='black')
axis[1, 0].hist(data3, bins=10, color='skyblue', edgecolor='black')
axis[1, 1].hist(data4, bins=10, color='skyblue', edgecolor='black')
plt.show()
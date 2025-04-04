import random
import numpy as np
from numpy.linalg import matrix_power

# x**4+x**3+1
# x**5+x**4+x**2+x**1+1
function = input('Введите функцию ->')
k = int(input('Введите k ->'))
X_st = function.split('+')
st = []
for i in X_st:
    if i.split('**')[0] != '1':
        st.append(int(i.split('**')[1]))

st = sorted(st)
N = st[-1]
print(f'k = {k}')
print(f'N = {N}')

#   Первая строка матрицы T
T = np.array([[]])
for i in range(N):
    if i + 1 in st:
        T = np.append(T, 1)
    else:
        T = np.append(T, 0)

#   Остальные строки матрицы T
for i in range(N - 1):
    T_i = np.array([0]*N)
    T_i[i] = 1
    T = np.concatenate((T, T_i), axis=0)
else:
    T = T.reshape(N, len(T)//N).astype('int')

print(f'\tT:')
print(T)

V = matrix_power(T, k)
#   Мб доделать по красивее
V_new = []
for i in range(len(V)):
    V_new.append([])
    for y in range(len(V[i])):
        V_new[-1].append(V[i][y] % 2)
V = np.array(V_new)
print(f'\n\tV:')
print(V)

#   Создание какой-то системы, не знаю как называется
Q_t  = []
for i in range(len(V)):
    Q_t.append([])
    for y in range(len(V[i])):
        if V[i][y] == 1:
            Q_t[-1].append(y+1)

print(f'\nQ(t+1) = T^{k} * Q(t):')
for i in range(len(Q_t)):
    string = ''
    for y in range(len(Q_t[i])):
        string += f'q{Q_t[i][y]}(t) + '
    print(f'\tq{i+1}(t+1) = {string[:-3]}')
print()

#   Создание строки начального состояния
# while True:
#     start = random.choices('01', k=N)
#     if '1' not in start:
#         continue
#     else:
#         break

print(f'\tДиаграмма:')
start = ['1', '0', '0', '0', '0']
print(' '.join(start))
start_save = start
save = [start]
count = 0
#   Перебор всех состояний
while True:
    count += 1
    if count == 10000:
        print(f"За 10000 итераций не было найдено периода")
        break
    start_new = []
    for i in range(len(Q_t)):
        num = 0
        for y in range(len(Q_t[i])):
            num += int(start[Q_t[i][y] - 1])
        start_new.append(str(num % 2))
    if start_new == start:
        break
    start = start_new
    print(' '.join(start))
    if start_save == start:
        break
    save.append(start)
print(f'Всего различных комбинаций {len(save)}\n')

q_N = ['']*N
for i in range(len(save)):
    for y in range(N):
        q_N[y] += save[i][y]

for i in range(len(q_N)):
    string = ''.join(q_N[i])
    print(f'q{i+1} = {string}')

print(q_N[int(input("Какую вывести?"))-1])
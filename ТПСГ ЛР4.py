import numpy as np
from numpy.linalg import matrix_power


def find(function, k, number, start):
    X_st = function.split('+')
    st = []
    for i in X_st:
        if i.split('**')[0] != '1':
            st.append(int(i.split('**')[1]))

    st = sorted(st)
    N = st[-1]

    T = np.array([[]])
    for i in range(N):
        if i + 1 in st:
            T = np.append(T, 1)
        else:
            T = np.append(T, 0)

    for i in range(N - 1):
        T_i = np.array([0]*N)
        T_i[i] = 1
        T = np.concatenate((T, T_i), axis=0)
    else:
        T = T.reshape(N, len(T)//N).astype('int')

    V = matrix_power(T, k)
    V_new = []
    for i in range(len(V)):
        V_new.append([])
        for y in range(len(V[i])):
            V_new[-1].append(V[i][y] % 2)
    V = np.array(V_new)

    Q_t  = []
    for i in range(len(V)):
        Q_t.append([])
        for y in range(len(V[i])):
            if V[i][y] == 1:
                Q_t[-1].append(y+1)

    start = [str(i) for i in start]
    start_save = start
    save = [start]
    while True:
        start_new = []
        for i in range(len(Q_t)):
            num = 0
            for y in range(len(Q_t[i])):
                num += int(start[Q_t[i][y] - 1])
            start_new.append(str(num % 2))
        if start_new == start:
            break
        start = start_new
        if start_save == start:
            break
        save.append(start)
    print(f"По формуле 2^{N}-1 = {2**N - 1}\n"
          f"Счетом = {len(save)}")

    q_N = ['']*N
    for i in range(len(save)):
        for y in range(N):
            q_N[y] += save[i][y]
    return q_N[number - 1]

# function_array = ['x**5+x**4+x**3+x**1+1', 'x**2+x**1+1', 'x**6+x**5+x**3+x**2+1']
# start_array = ['10101', '10', '101010']
# function_array = ['x**5+x**3+x**2+x**1+1', 'x**3+x**2+1', 'x**6+x**5+1']
# start_array = ['11111', '111', '111111']
function_array = ['x**5+x**4+x**3+x**1+1', 'x**3+x**1+1', 'x**6+x**5+x**2+x**1+1']
start_array = ['11111', '111', '111111']
k_array = [4, 5, 4]
number_array = [2, 1, 3]


array = []
for i in range(3):
    print(f"\tРСЛОС {i+1}:")
    function = input(f"Введите функцию = ")
    k = int(input(f"Введите k = "))
    number = int(input(f"Введите какую последовательность вывести = "))
    start = input(f"Введите начальное состояние = ")
    # function = function_array[i]
    # k = k_array[i]
    # number = number_array[i]
    # start = start_array[i]
    Rlos = find(function, k, number, start)
    array.append(Rlos)

print(f"\n\nПолучились последовательности:")
for i in range(len(array)):
    print(f"\tРСЛОС {i + 1}:")
    print(array[i])


T = len(array[0]) * len(array[1]) * len(array[2])
print(f'Период = {int(T)}\n')

string1 = array[0] * (int(T / len(array[0])))
string2 = array[1] * (int(T / len(array[1])))
string3 = array[2] * (int(T / len(array[2])))


otvet = ''
for sim in range(int(T)):
    x1 = int(string1[sim]) * int(string2[sim])
    x2 = int(string2[sim]) * int(string3[sim])
    x3 = int(string3[sim])
    otvet += f'{(x1 + x2 + x3) % 2}'
print(otvet)

numbers = []
while len(otvet) != 0:
    if len(otvet) < 16:
        num = otvet
        otvet = ''
        numbers.append(str(int(num, 2)))
        continue
    else:
        num = otvet[0:16]
        otvet = otvet[16:]
        numbers.append(str(int(num, 2)))
print(' ')
print(' '.join(numbers))

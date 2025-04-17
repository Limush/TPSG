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
        T_i = np.array([0] * N)
        T_i[i] = 1
        T = np.concatenate((T, T_i), axis=0)
    else:
        T = T.reshape(N, len(T) // N).astype('int')

    V = matrix_power(T, k)

    V_new = []
    for i in range(len(V)):
        V_new.append([])
        for y in range(len(V[i])):
            V_new[-1].append(V[i][y] % 2)
    V = np.array(V_new)

    Q_t = []
    for i in range(len(V)):
        Q_t.append([])
        for y in range(len(V[i])):
            if V[i][y] == 1:
                Q_t[-1].append(y + 1)
    for i in range(len(Q_t)):
        string = ''
        for y in range(len(Q_t[i])):
            string += f'q{Q_t[i][y]}(t) + '

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
        if start_new == start: break
        start = start_new
        if start_save == start: break
        save.append(start)

    q_N = [''] * N
    for i in range(len(save)):
        for y in range(N):
            q_N[y] += save[i][y]
    else:
        return q_N[number - 1]


def LR4(function1, k1, number1, start1,
        function2, k2, number2, start2,
        function3, k3, number3, start3):
    array = [find(function1, k1, number1, start1),
             find(function2, k2, number2, start2),
             find(function3, k3, number3, start3)]

    T = len(array[0]) * len(array[1]) * len(array[2])

    string1, string2, string3 = array[0] * (int(T / len(array[0]))), array[1] * (int(T / len(array[1]))), array[2] * (int(T / len(array[2])))

    Binary_str = ''.join([f'{((int(string1[sim]) * int(string2[sim])) + (int(string2[sim]) * int(string3[sim])) + int(string3[sim])) % 2}' for sim in range(int(T))])

    numbers = []
    while len(Binary_str) != 0:
        numbers.append(int(Binary_str[0:8], 2))
        Binary_str = Binary_str[8:]
    return numbers
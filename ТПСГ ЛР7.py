from math import sqrt, erfc
import scipy
import mpmath

from Дополнение import LR1
from Дополнение import LR2
from Дополнение import LR3
from Дополнение import LR4


def array_to_bin(array):
    bin_str = ''
    for num in array:
        bin_str += bin(num)[2:]
    return bin_str


def Test_1(string):
    n = len(string)
    S_n = sum([1 if num == '1' else -1 for num in string])
    S_obs = round(abs(S_n) / sqrt(n), 6)
    P_value = round(erfc(round(S_obs/sqrt(2), 6)), 6)

    print(f"\t\tTest №1")
    print(f"n = {n}")
    print(f"S_n = {S_n}")
    print(f"S_obs = {S_obs}")
    print(f"P_value = {P_value}")
    print(f"{P_value} {'>' if P_value > 0.01 else '<='} 0,01\n=> Последовательность {'' if P_value > 0.01 else 'не '}прошла тест")


def Test_2(string):
    n = len(string)
    M = 100
    block = [string[i:i+M] for i in range(0, len(string) - (len(string) % M), M)]
    pi_block = [number.count('1') for number in block]
    N = len(pi_block)
    X_obs = 4 * M * sum([((number / M) - 0.5)**2 for number in pi_block])
    P_value = scipy.special.gammainc(N / 2, X_obs / 2)

    print(f"\n\t\tTest №2")
    print(f"n = {n}")
    print(f"M = {M}")
    print(f"N = {N}")
    print(f"X_obs = {round(X_obs, 6)}")
    print(f"P_value = {P_value}")
    print(f"{P_value} {'>' if P_value > 0.01 else '<='} 0,01\n=> Последовательность {'' if P_value > 0.01 else 'не '}прошла тест")


def Test_3(string):
    n = len(string)
    Pi = string.count('1') / n

    print(f"\n\t\tTest №3")
    print(f"n = {n}")
    print(f"pi = {Pi}")
    print(f"Проверяем условие:")
    if abs(Pi - 0.5) < 2 / sqrt(n):
        V = sum([1 if string[num - 1] != string[num] else 0 for num in range(1, len(string))]) + 1
        P_value = round(erfc(round((abs(V - 2 * n * Pi * (1 - Pi)))/(2 * sqrt(2 * n) * Pi * (1 - Pi)), 6)), 6)

        print(f"|{Pi} - 0.5| < 2/sqrt({n})\n=>{round(abs(Pi - 0.5), 6)} < {round(2 / sqrt(n), 6)}")
        print(f"V = {V}")
        print(f"P_value = {P_value}")
        print(f"{P_value} {'>' if P_value > 0.01 else '<='} 0,01\n=> Последовательность {'' if P_value > 0.01 else 'не '}прошла тест")
    else:
        print(f"|{Pi} - 0.5| >= 2/sqrt({n})\n=>{round(abs(Pi - 0.5), 6)} >= {round(2 / sqrt(n), 6)}\nТест не пройден")


print(f"\t\t\tПоследовательность 1:")
data1 = LR1(7, 106, 1283, 6075, 100)
Test_1(data1)
Test_2(data1)
Test_3(data1)

print(f"\n\t\t\tПоследовательность 2:")
data2 = LR2(41, 5, 59, 48, 577, 100)
Test_1(data2)
Test_2(data2)
Test_3(data2)

print(f"\n\t\t\tПоследовательность 3:")
data3 = LR3('x**13+x**2+1', 2, '1'*13, 1)
Test_1(data3)
Test_2(data3)
Test_3(data3)

print(f"\n\t\t\tПоследовательность 4:")
data4 = LR4('x**5+x**3+1', 1, 1, '11100',
            'x**4+1', 1, 1, '1101',
            'x**6+x**1+1', 1, 1, '100111')
Test_1(data4)
Test_2(data4)
Test_3(data4)

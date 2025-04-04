from prettytable import PrettyTable


def Nod(a, b, count=0):
    if a == 0 or b == 0:
        return 0
    while True:
        count += 1
        a, b = b, a % b
        if b == 0:
            return a


def decomposition(number):
    array = []
    while number != 1:
        for i in range(2, number - 1):
            if number % i == 0:
                array.append(i)
                number = number // i
                break
        else:
            array.append(number)
            break
    return array


def generate_PSP(a2, x0, a1, b, m):
    PSP = [x0]
    while True:
        x_next = (a2*PSP[-1]**2 + a1*PSP[-1] + b) % m
        if x_next in PSP:
            return len(PSP) - PSP.index(x_next)
        else:
            PSP.append(x_next)


def generate_PSP2(a2, x0, a1, b, m, numbers):
    PSP = [x0]
    count = 0
    while count != numbers:
        x_next = (a2*PSP[-1]**2 + a1*PSP[-1] + b) % m
        PSP.append(x_next)
        count += 1
    return PSP


def generate_PSP_x(PSP, numbers):
    PSP_x, Num_x = [], numbers
    while True:
        if numbers > len(PSP):
            PSP_x += PSP
            numbers -= len(PSP)
        else:
            PSP_x += PSP[0:numbers]
            return PSP_x


def Cheak_max_T(a2, x0, a1, b, m, PSP):
    def total_multiplier(m_vrem, num, count=0):
        while m_vrem % num == 0:
            count += 1
            m_vrem = m_vrem // num
        return count

    count_usl = 0
    #   НОД
    if Nod(b, m) == 1:
        count_usl += 1
        print('Пункт 1 (выполнено):\n\tb и m - взаимно простые')
    else:
        print('Пункт 1 (не выполнено):\n\tb и m - взаимно простые')

    #   Множители
    raz = decomposition(m)
    for num in raz:
        if num % 2 == 0:
            continue
        if (a1 - 1) % num != 0 or a2 % num != 0:
            print('Пункт 2 (не выполнено):\n\ta1 - 1 и a2 кратны для всех p, где p-нечетные простые делители m')
            break
    else:
        count_usl += 1
        print('Пункт 2 (выполнено):\n\ta1 - 1 и a2 кратны для всех p, где p-нечетные простые делители m')

    #   Система сравнений
    if m % 2 == 0:
        if m % 4 == 0:
            if a2 % 4 == (a1 - 1) % 4:
                count_usl += 1
                print('Пункт 3 (выполнено):\n\tm - четное, a2 сравнимо с (a1-1)mod4, если m кратно 4 или a2 сравнимо с (a1-1)mod2, если m кратно 2')
            else:
                print('Пункт 3 (не выполнено):\n\tm - четное, a2 сравнимо с (a1-1)mod4, если m кратно 4 или a2 сравнимо с (a1-1)mod2, если m кратно 2')
        else:
            if a2 % 2 == (a1 - 1) % 2:
                count_usl += 1
                print('Пункт 3 (выполнено):\n\tm - четное, a2 сравнимо с (a1-1)mod4, если m кратно 4 или a2 сравнимо с (a1-1)mod2, если m кратно 2')

            else:
                print('Пункт 3 (не выполнено):\n\tm - четное, a2 сравнимо с (a1-1)mod4, если m кратно 4 или a2 сравнимо с (a1-1)mod2, если m кратно 2')
    else:
        print('Пункт 3 (не выполнено):\n\tm - четное, a2 сравнимо с (a1-1)mod4, если m кратно 4 или a2 сравнимо с (a1-1)mod2, если m кратно 2')

    #   4 условие
    if m % 9 == 0:
        if a2 % 9 != (3 * b) % 9:
            count_usl += 1
            print('Пункт 4 (выполнено):\n\tЕсли m кратно 9, то a2 не сравнимо с 3b(mod9)')
        else:
            print('Пункт 4 (не выполнено):\n\tЕсли m кратно 9, то a2 не сравнимо с 3b(mod9)')
    else:
        count_usl += 1
        print('Пункт 4 (выполнено):\n\tЕсли m кратно 9, то a2 не сравнимо с 3b(mod9)')

    return 1 if count_usl == 4 else 0


def inference(array):
    if len(array) % 20 == 0:
        for i in range(20):
            array.append('')
    else:
        for i in range(20 - (len(array) % 20)):
            array.append('')

    table = PrettyTable()
    for i in range(len(array) // 20):
        table.add_row([array[0 + i * 20], array[1 + i * 20], array[2 + i * 20], array[3 + i * 20], array[4 + i * 20],
                       array[5 + i * 20], array[6 + i * 20], array[7 + i * 20], array[8 + i * 20], array[9 + i * 20],
                       array[10 + i * 20], array[11 + i * 20], array[12 + i * 20], array[13 + i * 20],
                       array[14 + i * 20],
                       array[15 + i * 20], array[16 + i * 20], array[17 + i * 20], array[18 + i * 20],
                       array[19 + i * 20]])
    table.border = False
    table.header = False
    return table


a2 = 2
x0 = 5
a1 = 1
b = 3
m = 6
numbers = 10
PSP = generate_PSP(a2, x0, a1, b, m)
PSP2 = generate_PSP2(a2, x0, a1, b, m, numbers)
PSP_x = generate_PSP_x(PSP2, numbers)

print(f"Формула:\n"
      f"\tXₙ₊₁ = ({a2}Xₙ² + {a1}Xₙ + {b})mod {m}\n"
      f"Период последовательности = {PSP}\n")
non_compliance = Cheak_max_T(a2, x0, a1, b, m, PSP)
print(f"Период последовательности максимальный\n" if non_compliance == 1 else "")
print(f"Первые {numbers} элементов последовательности:\n{inference(PSP_x)}\n")

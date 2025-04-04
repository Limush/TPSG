from prettytable import PrettyTable


def Nod(a, b, count=0):
    while True:
        count += 1
        a, b = b, a % b
        if b == 0:
            return a


def decomposition(number, array):
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


def generate_PSP(x0, a, b, m):
    PSP = [str(x0)]
    while True:
        if len(PSP) > 10000000:
            break
        x_next = str((a * int(PSP[-1]) + b) % m)
        if x_next in PSP:
            break
        else:
            PSP.append(x_next)
    return PSP


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


def Cheak_max_T(x0, a, b, m, PSP):
    def total_multiplier(m_vrem, num, count=0):
        while m_vrem % num == 0:
            count += 1
            m_vrem = m_vrem // num
        return count

    if b == 0:
        if m % 10 == 0:
            q = total_multiplier(m, 10)
            if q >= 5 and x0 % 2 != 0 and x0 % 5 != 0:
                print(f"Для МКГ если m=10**{q}, q>=5 и x0 не кратно 2 и 5, то максимальный период:\n"
                      f"-> T_max = 5*10^(q-1)=m/2")
                return 5 * (10 ** (q - 1)), 0
        if m % 2 == 0:
            q = total_multiplier(m, 2)
            if q >= 4:
                print(f"Для МКГ если m=2**{q}, q>=2, то максимальный период:\n"
                      f"-> T_max = 5*10^(q-1)=m/2")
                return 2 ** (q - 2), 0
    else:
        if Nod(b, m) == 1:
            multipliers = decomposition(m, [])
            for i in range(len(multipliers)):
                if Nod(multipliers[i], a - 1) != 1:
                    break
            else:
                return False, 2
            if m % 4 == 0:
                if (a - 1) % 4 == 0:
                    return len(PSP), 0
                else:
                    return False, 2
            else:
                return len(PSP), 0
    return False, 1


x0, a, b, m, ckolko = 1, 106, 0, 2048, 199
PSP = generate_PSP(x0, a, b, m)
T_max, non_compliance = Cheak_max_T(x0, a, b, m, PSP)

print(f"При значениях:\n\tx0={x0}\n\ta={a}\n\tb={b}\n\tm={m}\nПериод последовательности = {len(PSP)}")
if T_max and non_compliance == 0:
    print(f"Максимальный период = {T_max}")
else:
    print(f"Данная последовательность не имеет максимальны период для m = {m}")
    if non_compliance == 1:
        print(f"Не соблюдено условие 1:\n\tb = {b} и m = {m} не взаимно простые")
    elif non_compliance == 2:
        print(f"Не соблюдено условие 2:\n\ta-1 = {a - 1} должно быть кратно p, где p простые множители числа m = {m}")
    else:
        print(f"Не соблюдено условие 3:\n\tm = {m} кратно 4, а = {a} не кратно 4")

PSP_x, Num_x = [], ckolko
while True:
    if ckolko > len(PSP):
        PSP_x += PSP
        ckolko -= len(PSP)
    else:
        PSP_x += PSP[0:ckolko]
        break

print(f"Первые {Num_x} элементов последовательности:\n{inference(PSP_x)}\n")

print(f"Элементы последовательности:\n{inference(PSP)}")

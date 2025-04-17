def LR1(x0, a, b, m, ckolko):
    def generate_PSP(x0, a, b, m):
        PSP = [x0]
        while True:
            if len(PSP) > 10000000:
                break
            x_next = (a * int(PSP[-1]) + b) % m
            if x_next in PSP:
                break
            else:
                PSP.append(x_next)
        return PSP

    PSP = generate_PSP(x0, a, b, m)
    PSP_x, Num_x = [], ckolko
    while True:
        if ckolko > len(PSP):
            PSP_x += PSP
            ckolko -= len(PSP)
        else:
            PSP_x += PSP[0:ckolko]
            break
    return PSP_x

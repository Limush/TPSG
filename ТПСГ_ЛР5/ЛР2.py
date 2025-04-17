def LR2(a2, x0, a1, b, m, numbers):
    def generate_PSP(a2, x0, a1, b, m, numbers):
        PSP = [x0]
        PSP_len = -1
        count = 0
        while True:
            x_next = (a2 * PSP[-1] ** 2 + a1 * PSP[-1] + b) % m
            count += 1
            if x_next in PSP and PSP_len == -1:
                PSP_len = len(PSP) - PSP.index(x_next)
            PSP.append(x_next)
            if count >= numbers and PSP_len != -1:
                return PSP[0:numbers]
    return generate_PSP(a2, x0, a1, b, m, numbers)
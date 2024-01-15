def white_stalkers(village: str) -> bool:
    if len(village) < 5:
        return False
    return find_stalkers(village, 0, 0, 0, 0)


def find_stalkers(village, i, sum_d, sum_v, flag):
    if i == len(village):
        if flag >= 1:
            return True
        return False
    value = village[i]
    if sum_d and value == '=':
        sum_v += 1
    elif value.isdigit():
        sum_d += int(value)
        if sum_d == 10 and sum_v != 3:
            return False
        elif sum_d == 10 and sum_v == 3:
            flag += 1
            sum_d = int(value)
            sum_v = 0
    return find_stalkers(village, i+1, sum_d, sum_v, flag)



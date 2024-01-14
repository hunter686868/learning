def white_stalkers(village: str) -> bool:
    return find_stalkers(village, 0, 0, 0)


def find_stalkers(village, i, sum_d, sum_v):
    if i == len(village):
        return False
    value = village[i]
    if value.isdigit():
        sum_d += int(value)
    elif value == '=':
        sum_v += 1
    if sum_d == 10 and sum_v == 3:
        return True
    return find_stalkers(village, i+1, sum_d, sum_v)


print(white_stalkers('abc=7==hdjs=3gg1=======5'))
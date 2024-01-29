def TRC_sort(trc: list) -> list:
    if len(trc) < 2:
        return trc
    result = [[], [], []]
    for i in trc:
        result[i].append(i)
    return result[0] + result[1] + result[2]

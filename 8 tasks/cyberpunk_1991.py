def artificial_muscle_fibers(arr: list) -> int:
    lst = {}
    cnt = 0
    for i in arr:
        if i not in lst:
            lst[i] = 0
        else:
            lst[i] += 1
            if lst[i] == 1:
                cnt += 1
            else:
                continue
    return cnt

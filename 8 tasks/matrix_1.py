def digital_rain(col):
    zero = 0
    one = 0
    max_len = 0
    max_str = ""
    diff = {0: 0}

    for i in range(len(col)):
        if int(col[i]) == 0:
            zero += 1
        else:
            one += 1
        df = zero - one
        if df in diff:
            cur_len = i - diff[df]
            if cur_len >= max_len:
                max_len = cur_len
                max_str = col[diff[df]+1: i+1]
        else:
            diff[df] = i
    return max_str

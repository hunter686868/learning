def digital_rain(col):
    zero = 0
    one = 0
    max_len = 0
    max_str = ""

    for i in reversed(range(len(col))):
        if int(col[i]) == 0:
            zero += 1
        else:
            one += 1
        equality = zero == one
        if equality:
            curr_len = zero + one
            if i + curr_len > max_len:
                max_len = curr_len
                max_str = col[i:i + curr_len]

    return max_str


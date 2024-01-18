def digital_rain(col: str) -> str:
    if len(col) < 2:
        return ''
    return find_substring(col, 0, 0, 0, '')


def find_substring(col, i, zero, one, max_len):
    if len(col) == i:
        return max_len
    value = col[i]
    if int(value) == 0:
        zero += 1
    else:
        one += 1
    if zero == one:
        cur_len = zero + one
        max_len = col[i - cur_len + 1:i + 1]
    return find_substring(col, i + 1, zero, one, max_len)


print(digital_rain('011111110'))

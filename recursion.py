def exponentiation(n, m):
    if m == 0:
        return 1
    else:
        return n * exponentiation(n, m - 1)


print(exponentiation(4, 2))


def digits_sum(number):
    if number < 10:
        return number
    else:
        return number % 10 + digits_sum(number // 10)


print(digits_sum(13333))


def list_len(lst):
    if not lst:
        return 0
    else:
        lst.pop()
        return 1 + list_len(lst)


print(list_len([1, 2, 4, 1, 3, 2, 5, 6, 8]))


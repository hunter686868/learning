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




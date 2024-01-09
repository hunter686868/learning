def exponentiation(n, m):
    if m == 0:
        return 1

    return n * exponentiation(n, m - 1)


print(exponentiation(4, 2))


def digits_sum(number):
    if number < 10:
        return number

    return number % 10 + digits_sum(number // 10)


print(digits_sum(13333))


def list_len(lst):
    if not lst:
        return 0

    lst.pop(0)
    return 1 + list_len(lst)


print(list_len([1, 2, 4, 1, 2, 5, 6, 8]))


def palindrome(string):
    if len(string) < 2:
        return True
    if string[0] != string[-1]:
        return False
    return palindrome(string[1: -1])


print(palindrome('3334444333'))


def even_numbers(lst):
#    if
def exponentiation(n, m):
    if m == 0:
        return 1

    return n * exponentiation(n, m - 1)


#print(exponentiation(4, 2))


def digits_sum(number):
    if number < 10:
        return number

    return number % 10 + digits_sum(number // 10)


#print(digits_sum(13333))


def list_len(lst):
    if not lst:
        return 0
    lst.pop(0)
    return 1 + list_len(lst)


#print(list_len([1, 2, 4, 1, 2, 5, 6, 8]))


def palindrome(string):
    if len(string) < 2:
        return True
    return chk_plndr(string, 0)


def chk_plndr(string, i):
    if i >= len(string)/2:
        return True
    if string[i] != string[-i - 1]:
        return False
    return chk_plndr(string, i + 1)


#print(palindrome('lev3el'))


def even_numbers(lst):
    return chk_even_n(lst, 0)


def chk_even_n(lst, i):
    if i == len(lst):
        return []
    if lst[i] % 2 == 0:
        return [lst[i]] + chk_even_n(lst, i + 1)
    return chk_even_n(lst, i + 1)


#print(even_numbers([1,2,3,4,5,6,7,8,9, 14, 16, 15,2,2,2,2,2]))
#print(even_numbers([]))


def even_index(lst):
    return chk_even_i(lst, 0)


def chk_even_i(lst, i):
    if i >= len(lst):
        return []
    return [lst[i]] + chk_even_i(lst, i + 2)


#print(even_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4]))


def second_max(lst):
    if len(lst) < 2:
        return False
    return find_second_max(lst, 0, lst[0], lst[0])


def find_second_max(lst, i, m1, m2):
    if i == len(lst):
        return m2
    n = lst[i]
    if n > m1:
        return find_second_max(lst, i + 1, n, m2)
    if n > m2:
        return find_second_max(lst, i + 1, m1, n)
    return find_second_max(lst, i + 1, m1, m2)


#print(second_max([11, 2, 10, 10, 4, 5, 12, 7]))


import os
def files(path)
    os.

def find_files(path, )

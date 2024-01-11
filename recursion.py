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
    if string[i] == string[-i - 1]:
        return chk_plndr(string, i + 1)
    return False


print(palindrome('ооопооо'))


def even_numbers(lst):
    a = lst
    if not lst:
        return []
    a.pop(0)
    if lst[0] % 2 == 0:
        return [lst[0]] + even_numbers(a)
    return even_numbers(a)


#print(even_numbers([1,2,3,4,5,6,7,8,9, 14, 16, 15]))


def even_index(lst):
    if not lst:
        return []
    even = lst.pop(0)
    if not lst:
        return [even]
    lst.pop(0)
    return [even] + even_index(lst)


#print(even_index([1,2,3,4,5,6,7,8,9]))

def second_max(lst):
    if len(lst) < 2:
        return False
    return max()

#def max(sl):



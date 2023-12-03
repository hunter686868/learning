a = input('Строка')
b = input('Подстрока')


def func(s1, s2):
    for i in range(len(s1) - len(s2) + 1):
        for j in range(len(s2)):
            if s1[i + j] != s2[j]:
                break
            elif j == len(s2) - 1:
                return True
    return False


print(func(a, b))
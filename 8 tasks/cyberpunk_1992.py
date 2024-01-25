def massdriver(activate: list) -> int:
    dct = {}
    lst = []
    for i in range(len(activate)):
        if activate[i] in dct:
            lst.append(dct[activate[i]])
        else:
            dct[activate[i]] = i
    if lst:
        return min(lst)
    return -1


print(massdriver([1,2,3,1,2,3,4]))# = 0
print(massdriver([1,2,3,4,3,4,2]))# = 1
print(massdriver([1,2,3,4,5,6,7]))# = -1)


def massdriver(activate: list) -> int:
    for i in range(len(activate)):
        if activate.count(activate[i]) > 1:
            return i
    return -1


print(massdriver([1,2,3,1,2,3,4]))# = 0
print(massdriver([1,2,3,4,3,4,2]))# = 1
print(massdriver([1,2,3,4,5,6,7]))# = -1)
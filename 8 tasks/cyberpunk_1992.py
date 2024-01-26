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

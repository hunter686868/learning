def massdriver(activate: list) -> int:
    for i in range(len(activate)):
        if activate.count(activate[i]) > 1:
            return i
    return -1

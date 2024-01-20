def eec_help(arr1: list, arr2: list) -> bool:
    if len(arr1) != len(arr2):
        return False
    for i in arr1:
        if i in arr2 and arr1.count(i) == arr2.count(i):
            continue
        else:
            return False
    return True

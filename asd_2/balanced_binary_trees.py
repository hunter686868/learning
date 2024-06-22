def GenerateBBSTArray(a):
    if not a:
        return []
    a.sort()

    def create_bbst(arr, start, end):
        if start > end:
            return []
        middle_index = (end + start)//2
        middle_item = arr[middle_index]
        left_subtree = create_bbst(arr, start, middle_index - 1)
        right_subtree = create_bbst(arr, middle_index + 1, end)
        return [middle_item] + left_subtree + right_subtree
    return create_bbst(a, 0, len(a) - 1)


t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(GenerateBBSTArray(t))


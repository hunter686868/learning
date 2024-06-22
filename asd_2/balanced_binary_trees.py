def GenerateBBSTArray(a):
    if a is None:
        return []
    a.sort()
    def create_bbst(a, start, end):
        if start > end:
            return []
        middle_index = (start + end)//2
        middle_item = a[middle_index]
        left_subtree = create_bbst(a, start, middle_item - 1)
        right_subtree = create_bbst(a, middle_item + 1, end)
        return [middle_item] + left_subtree + right_subtree
    return create_bbst(a, 0, len(a) - 1)



a = [2, 1, 3, 5, 4, 6, 9, 7, 8, 0]
b = GenerateBBSTArray(a)
print(b)
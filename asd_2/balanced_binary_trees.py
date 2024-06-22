def GenerateBBSTArray(a):
    if not a:
        return []
    a.sort()

    def create_bbst(a, start, end):
        if start > end:
            return []
        middle_index = (start + end)//2
        middle_item = a[middle_index]
        left_subtree = create_bbst(a, start, middle_index - 1)
        right_subtree = create_bbst(a, middle_index + 1, end)
        return [middle_item] + left_subtree + right_subtree
    return create_bbst(a, 0, len(a) - 1)


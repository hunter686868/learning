def GenerateBBSTArray(a):

    a.sort()
    result_array = [None] * len(a)

    def create_bbst(arr, start, end, result, i):
        if start > end:
            return
        middle_index = (end + start)//2
        result[i] = arr[middle_index]
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        if left_child < len(result):
            create_bbst(arr, start, middle_index - 1, result, left_child)
        if right_child < len(result):
            create_bbst(arr, middle_index + 1, end, result, right_child)

    create_bbst(a, 0, len(a) - 1, result_array, 0)
    return result_array


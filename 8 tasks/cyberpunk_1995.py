def army_communication_matrix(n, matrix):
    if n < 2:
        return []
    max_sum = float('-inf')
    start_end = [0, 0, 0, 0]

    for left in range(n):
        temp = [0] * n
        for right in range(left, n):
            for i in range(n):
                temp[i] += matrix[i][right]

            curr_sum = 0
            curr_st_row = 0

            for i in range(n):
                if curr_sum <= 0:
                    curr_sum = temp[i]
                    curr_st_row += 1
                else:
                    curr_sum += temp[i]

                if curr_sum > max_sum:
                    max_sum = curr_sum
                    start_end[0] = curr_st_row
                    start_end[1] = i
                    start_end[2] = left
                    start_end[3] = right

    size = start_end[3] - start_end[2]
    return f'{start_end[0]}, {start_end[2]}, {size}'


nn = 3
mx = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(army_communication_matrix(nn, mx))

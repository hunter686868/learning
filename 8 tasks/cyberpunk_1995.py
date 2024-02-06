def army_communication_matrix(n, matrix):
    if n < 2:
        return []
    max_sum = float('-inf')
    start_end = [0, 0, 0, 0]
    temp = []
    for y in range(n):
        temp.append([0] * n)
        for x in range(n):
            if x == y == 0:
                temp[0][0] = matrix[0][0]
            elif y == 0:
                temp[0][x] = temp[0][x-1] + matrix[0][x]
            elif x == 0:
                temp[y][0] = temp[y-1][0] + matrix[y][0]
            else:
                temp[y][x] = temp[y-1][x] + temp[y][x-1] - temp[y-1][x-1] + matrix[y][x]

    for x1 in range(n):
        for y1 in range(n):
            for x2 in range(x1, n):
                for y2 in range(y1, n):
                    if x1 == x2 == 0:
                        curr_sum = temp[y2][x2]
                    elif y1 == 0:
                        curr_sum = temp[y2][x2] - temp[y1 - 1][x2]
                    elif x1 == 0:
                        curr_sum = temp[y2][x2] - temp[y1 - 1][x2]
                    else:
                        curr_sum = temp[y2][x2] + temp[y1 - 1][x1 - 1] - temp[y1 - 1][x2] - temp[y2][x1 - 1]
                    if curr_sum > max_sum and x2 - x1 == y2 - y1:
                        max_sum = curr_sum
                        start_end[0] = x1
                        start_end[1] = y1
                        start_end[2] = x2
                        start_end[3] = y2

    return start_end[0], start_end[1], (start_end[3] - start_end[0])


nn = 3
mx = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(army_communication_matrix(nn, mx))

nnn = 4
mxx = [
    [1, 9, 2, 3],
    [4, 8, 5, 6],
    [0, 7, 1, 2],
    [0, 0, 0, 0]
]

print(army_communication_matrix(nnn, mxx))

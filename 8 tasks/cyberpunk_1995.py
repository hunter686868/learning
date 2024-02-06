def army_communication_matrix(n, matrix):
    if n < 2:
        return []
    max_sum = float('-inf')
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

    for y1 in range(n):
        for x1 in range(n):
            for y2 in range(y1, n):
                for x2 in range(x1, n):
                    if x1 == x2 == 0:
                        curr_sum = temp[y2][x2]
                    elif y1 == 0:
                        curr_sum = temp[y2][x2] - temp[y2][x1 - 1]
                    elif x1 == 0:
                        curr_sum = temp[y2][x2] - temp[y1 - 1][x2]
                    else:
                        curr_sum = temp[y2][x2] + temp[y1 - 1][x1 - 1] - temp[y1 - 1][x2] - temp[y2][x1 - 1]
                    if curr_sum > max_sum and x2 - x1 == y2 - y1:
                        max_sum = curr_sum
                        x1max = x1
                        y1max = y1
                        size = y2 - y1 + 1

    return f'{x1max} {y1max} {size}'

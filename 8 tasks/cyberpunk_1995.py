def army_communication_matrix(n, matrix):
    if n < 2 or n >= len(matrix):
        return []


nn = 3
mx = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(army_communication_matrix(nn, mx))

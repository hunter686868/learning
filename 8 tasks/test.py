def spiral_traversal_recursive(matrix, top, bottom, left, right, result):
    if top > bottom or left > right:
        return

    for i in range(left, right + 1):
        result.append(matrix[top][i])
    top += 1

    for i in range(top, bottom + 1):
        result.append(matrix[i][right])
    right -= 1

    if top <= bottom:
        for i in range(right, left - 1, -1):
            result.append(matrix[bottom][i])
        bottom -= 1

    if left <= right:
        for i in range(bottom, top - 1, -1):
            result.append(matrix[i][left])
        left += 1

    spiral_traversal_recursive(matrix, top, bottom, left, right, result)

def spiral_traversal(matrix):
    result = []
    spiral_traversal_recursive(matrix, 0, len(matrix) - 1, 0, len(matrix[0]) - 1, result)
    return result

# Пример использования
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = spiral_traversal(matrix)
print(result)

def tr_matrix(top, bottom, left, right, mx, result):
    assert top <= bottom
    assert left <= right
    if top > bottom or left > right:
        return result
    for i in range(left, right + 1):
        result.append(mx[top][i])
    top += 1
    for i in range(top, bottom + 1):
        result.append(mx[i][right])
    right -= 1
    if top <= bottom:
        for i in reversed(range(left, right + 1)):
            result.append(mx[bottom][i])
        bottom -= 1
    if left <= right:
        for i in reversed(range(top, bottom + 1)):
            result.append(mx[i][left])
        left += 1
    return tr_matrix(top, bottom, left, right, mx, result)


def matrix(n, m, matrix):
    assert n >= 0 and m >= 0
    return tr_matrix(0, m - 1, 0, n - 1, matrix, [])

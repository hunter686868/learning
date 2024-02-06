def max_submatrix1(matrix):
  height = len(matrix)
  width = len(matrix[0])

  maxsum = 0
  for y1 in range(height):
    for x1 in range(width):
      for y2 in range(y1, height):
        for x2 in range(x1, width):
          # Вычисляем сумму элементов для матрицы x1,y1-x2,y2
          subsum = 0
          for y in range(y1, y2+1):
            for x in range(x1, x2+1):
              subsum += matrix[y][x]
          if maxsum == None or subsum > maxsum:
            maxsum = subsum
            x1max = x1
            y1max = y1
            x2max = x2
            y2max = y2

  return (maxsum, (x1max, y1max), (x2max, y2max))

# Метод 2. Вычисляем все субматрицы subsum0, начинающиеся в точке (0,0), затем для
# нахождения суммы матрицы x1,y1-x2,y2 используем формулу subsum(x1,y1,x2,y2) =
# = subsum0(x2,y2) + subsum0(x1-1,y1-1) - subsum0(x2,y1-1) - subsum0(x1-1,y2).
# Сложность O((N*M)^2).
# Возвращает максимальную сумму и координаты 4-х точек как (sum, (x1, y1), (x2, y2)).
# Отсчёт с 0.
def max_submatrix2(matrix):
  height = len(matrix)
  width = len(matrix[0])

  # Предвариетльное вычисление сумм элементов матриц 0,0-x,y
  subsum0 = []
  for y in range(height):
    subsum0.append([])
    for x in range(width):
      if x == y == 0:  # верхняя левая точка
        subsum0[0].append(matrix[0][0])
      elif y == 0:  # верхняя строка
        subsum0[0].append(subsum0[0][x-1] + matrix[0][x])
      elif x == 0:  # левый столбец
        subsum0[y].append(subsum0[y-1][0] + matrix[y][0])
      else:
        subsum0[y].append(subsum0[y-1][x] + subsum0[y][x-1] - \
          subsum0[y-1][x-1] + matrix[y][x])

  # Поиск подматрицы с максимальной суммой элементов
  maxsum = None
  for y1 in range(height):
    for x1 in range(width):
      for y2 in range(y1, height):
        for x2 in range(x1, width):
          # Вычисляем сумму элементов для матрицы x1,y1-x2,y2
          if x1 == y1 == 0:  # начало - верхняя левая точка
            subsum = subsum0[y2][x2]
          elif y1 == 0:  # начало - верхняя строка
            subsum = subsum0[y2][x2] - subsum0[y2][x1-1]
          elif x1 == 0:  # начало - левый столбец
            subsum = subsum0[y2][x2] - subsum0[y1-1][x2]
          else:
            subsum = subsum0[y2][x2] + subsum0[y1-1][x1-1] - \
              subsum0[y1-1][x2] - subsum0[y2][x1-1]
          if subsum > maxsum and x2 - x1 < width:
            maxsum = subsum
            x1max = x1
            y1max = y1
            x2max = x2
            y2max = y2

  return (maxsum, (x1max, y1max), (x2max, y2max))

########################################################################################

def calc_and_show(matrix):
  r = max_submatrix1(matrix)
  print(f'Method1. Max sum = {r[0]}, coordinates: ({r[1][1]+1},{r[1][0]+1}), ({r[2][1]+1},{r[2][0]+1})')
  r = max_submatrix2(matrix)
  print(f'Method2. Max sum = {r[0]}, coordinates: ({r[1][1]+1},{r[1][0]+1}), ({r[2][1]+1},{r[2][0]+1})')
  print()

calc_and_show(
  ((1, 2, 3),
   (4, 5, 6),
   (7, 8, 9)))

calc_and_show(
  (( 0, -1,  2, -3,  1),
   (-1,  1, -4,  7, -2),
   ( 1,  1,  2,  6, -5),
   (-1, -5, -3, 10,  1),
   (-1,  9,  3,  1,  1),
   ( 2,  1, -4,  0,  1)))

print('p.s. Coordinates: Y then X, starting from 1.')
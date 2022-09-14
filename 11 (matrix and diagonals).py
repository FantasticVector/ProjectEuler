from math import prod
with open('./ProjectEuler/11_input.txt') as f:
  temp = f.read().splitlines()
  matrix = [list(map(int, i.split())) for i in temp]

vertical = []
horizontal = []
diagonal1 = []
diagonal2 = []
for i in range(20):
  for j in range(17):
    vertical.append(matrix[i][j:j+4])
    horizontal.append([matrix[j][i], matrix[j+1][i], matrix[j+2][i], matrix[j+3][i]])
    if i < 17:
      diagonal1.append([matrix[i][j], matrix[i+1][j+1], matrix[i+2][j+2], matrix[i+3][j+3]])
      diagonal2.append([matrix[i][j+3], matrix[i+1][j+2], matrix[i+2][j+1], matrix[i+3][j]])
max = 0
for v in [*vertical, *diagonal1, *diagonal2, *horizontal]:
  if prod(v) > max: max = prod(v)
print(max)
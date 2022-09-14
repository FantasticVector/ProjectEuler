size = 21

def pat(arr):
  for i in arr:
    print(i)

mat = [[0 for _ in range(size+1)] for i in range(size+1)]

mat[1][1] = 1

for i in range(size+1):
  for j in range(size+1):
    if j < size:
      mat[i][j+1] += mat[i][j]
    if i < size:
      mat[i+1][j] += mat[i][j]
pat(mat)
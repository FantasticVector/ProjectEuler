def isPentagonal(num):
  return (((24*num+1)**0.5 + 1)/6)%1 == 0

notFound = True
i = 1
result = 0
while notFound:
  i += 1
  n = i*(3*i-1)/2
  for j in reversed(range(1, i)):
    m = j*(3*j-1)/2
    if isPentagonal(n-m) and isPentagonal(n+m):
      result = n-m
      notFound = False
      break

print(result)
def sumOfDiagonals(n):
  n = n//2
  return (3+2*n*(8*n**2+15*n+13))/3

print(sumOfDiagonals(1001))
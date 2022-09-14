from math import factorial
def combination(n, r):
  return int(factorial(n)/(factorial(r)*factorial(n-r)))
count = 0
for n in range(1, 101):
  for r in range(1, n+1):
    if combination(n, r) > 10**6: count+=1

print(count)
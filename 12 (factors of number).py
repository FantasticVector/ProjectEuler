from functools import reduce 

def countFactors(n):
  return len(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5)+1) if n % i == 0))))

i = 1
while True:
  num = i*(i+1)/2
  if countFactors(num) > 500: break
  i += 1
print(num)

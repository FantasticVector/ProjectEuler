import math

def divisors(n):
  divs = [1]
  for i in range(2, int(math.sqrt(n))+1):
    if n%i == 0:
      divs.extend([i, n//i])
  return list(set(divs))

value = 0
for num in range(1, 10000):
  a = sum(divisors(num))
  b = sum(divisors(a))
  if num == b and a != b: 
    print(num)
    value+=num

print(value)
n = 12
from math import sqrt
# def fib(num):
#   return ((1+sqrt(5))**num - (1 - sqrt(5))**num)/(2**n*sqrt(5))

a, b = 0, 1
count = 0
while True:
  count+=1
  if len(str(b)) == 1000: break
  a, b = b, a + b
print(count)
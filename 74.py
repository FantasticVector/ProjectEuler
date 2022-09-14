from math import factorial
def factChain(num):
  memo = []
  while num not in memo:
    memo.append(num)
    num = sum([factorial(int(x)) for x in str(num)])
  return len(memo)

count = 0
memo = {}
for num in range(1000000):
  if factChain(num) == 60:
    count+=1
print(count)
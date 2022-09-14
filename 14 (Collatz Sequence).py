cache = {1:1}
def collatz(n):
  path = [n]
  while n not in cache:
    if n%2: n = n*3 + 1
    else: n = n/2
    path.append(n)
  for i, m in enumerate(reversed(path)):
    cache[m] = cache[n] + i  
  return cache[path[0]]

num = 0
max = 0
for i in range(1, 1000000):
  if collatz(i) > max: 
    num = i
    max = collatz(i)
print(num)




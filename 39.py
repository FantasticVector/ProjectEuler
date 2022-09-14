cache = {}
for a in range(1000):
  for b in range(a, 1000):
    c = (a**2+b**2)**(0.5)
    if c%1 == 0 and a+b+c<=1000:
      if a+b+c not in cache: cache[int(a+b+c)] = 0
      else: cache[int(a+b+c)] += 1
print(sorted(cache.items(), key=lambda x: x[1], reverse=True))
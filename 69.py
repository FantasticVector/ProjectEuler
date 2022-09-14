def factors(num):
  a = set()
  for i in range(2, int(num**.5)+1):
    if num%i == 0:
      a.add(i)
      a.add(num//i)
  return sorted(a)

print(factors(10))
for i in range(10):
  for fact in facts:
    if i%fact != 0:
      

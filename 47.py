def primeFactors(num):
  fact = []
  c = 2
  while num > 1:
    if num % c == 0: 
      fact.append(c)
      num = num/c
    else: 
      c = c + 1 
  return fact

for i in range(1000000):
  a, b = set(primeFactors(i)), set(primeFactors(i+1))
  c, d = set(primeFactors(i+2)), set(primeFactors(i+3))

  if [len(a), len(b), len(c), len(d)] == [4, 4, 4 ,4]:
    print(i)
    break
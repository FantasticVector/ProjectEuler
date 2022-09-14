def isPrime(num):
  if num < 2: return False
  for i in range(2, int(num**0.5)+1):
    if num%i == 0: return False
  return True

def rlDigits(num):
  patt = [num]
  for i in range(1, len(str(num))):
    patt.append(int(str(num)[i:]))
    patt.append(int(str(num)[:i]))
  return patt

primes = {i for i in range(1000000) if isPrime(i)}
values = []
for i in range(10, 1000000):
  if set(rlDigits(i))<=primes:
    values.append(i)

print(values)
print(sum(values))
def isPrime(num):
  for i in range(2, int((num**0.5))+1):
    if num%i == 0: return False
  return True

def isNPandigital(num):
  digits = len(str(num))
  return set(str(num)) == set('123456789'[:digits])

cache = set()
for i in range(10**7):
  if isNPandigital(i) and isPrime(i):
    cache.add(i)
print(sorted(cache))
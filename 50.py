def primeFactors(num):
  facts = []
  c = 2
  while num > 0:
    if num%c == 0:
      facts.append(c)
      num/=c
    else:
      c+=1
  return facts

def isPrime(num):
  for i in range(2, int(num**0.5)+1):
    if num%i == 0: return False
  return True
primes = [i for i in range(1, 10**3) if isPrime(i)]

for num in primes:
  facts = primeFactors(num)
  start = primes.index(min(facts))
  end = primes.index(max(facts))
  if facts == primes[start:end+1]:
    print(facts)
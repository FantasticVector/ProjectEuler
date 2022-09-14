def isPrime(num):
  for i in range(2, int(num**0.5)+1):
    if num%i == 0: return False
  return True

percent = 100
prime_count = 0
total_count = 1
n = 1
side = 1
while percent > 10:
  a = 4*n**2+1
  primes = sum([isPrime(a-2*n), isPrime(a), isPrime(a+2*n), isPrime(a+4*n)])
  prime_count += primes
  total_count += 4
  percent = (prime_count/total_count)*100
  side+=2
  n+=1
print(side)
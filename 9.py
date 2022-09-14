def isPrime(num):
  for i in range(2, int(num**(0.5))+1):
    if num % i == 0: return False
  return True

sum = 0
i = 2
while i < 2000000:
  if isPrime(i): sum+=i
  i += 1
  print(i)
print(sum)

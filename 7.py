from math import sqrt
def isPrime(num):
  for i in range(2, int(sqrt(num))+1):
    if num % i == 0: return False
  return True

i = 0
values = []
num = 2
while i < 10002:
   if isPrime(num): 
    i+=1
    values.append(num)
   num+=1
print(num)
print(values)
print(len(values))
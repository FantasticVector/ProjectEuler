def isPrime(num):
  for i in range(2, int((num)**0.5)+1):
    if num%i == 0: return False
  return True

def allRotations(num):
  values = [i for i in str(num)]
  rotations = []
  for i in range(len(values)):
    rotations.append(int(''.join(values[i:]+values[:i])))
  return rotations

values = []
for i in range(2, 1000000):
  if all([isPrime(r) for r in allRotations(i)]):
    values.append(i)
print(values)
print(len(values))

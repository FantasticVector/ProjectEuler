def isPandigital(num):
  return set(str(num)) == set('123456789')

values = []
for num in range(100000): #range(200):
  pand = ''
  i = 1
  while len(pand+str(num*i))<=9:
    pand += str(num*i)
    i+=1
  if isPandigital(pand): values.append(pand)

print(sorted(values))



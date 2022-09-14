from math import factorial
values=[]
for i in range(10, 1000000):
  facsum = sum([factorial(int(x)) for x in str(i)])
  if facsum == i: values.append(facsum)
print(values)
print(sum(values))
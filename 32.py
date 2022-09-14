values = []
for x in range(1, 100):
  for y in range(100, 10000):
    if sorted(str(x)+str(y)+str(x*y))==['1', '2', '3', '4', '5', '6', '7', '8', '9']:
      values.append(x*y)

print(sum(set(values)))
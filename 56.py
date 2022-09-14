max = 0
for i in range(100):
  for j in range(100):
    l = sum(map(int, list(str(i**j))))
    if l > max: max = l

print(max)
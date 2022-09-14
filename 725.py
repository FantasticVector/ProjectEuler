values = []
for i in range(1000000):
  val = list(map(int, set(str(i))))
  if max(val) == (sum(val) - max(val)):
    values.append(i)
print(sum(values))
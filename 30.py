ans = []
for i in range(10, 1000000):
  value = sum([int(x)**5 for x in str(i)])
  if value == i:
    ans.append(value)
print(sum(ans))
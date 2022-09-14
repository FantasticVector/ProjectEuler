sum = 0
for i in range(1001):
  sum+=int(str(i**i)[-10:])
print(sum)

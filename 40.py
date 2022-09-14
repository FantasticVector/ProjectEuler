value = ''
i = 1
while len(value)<1000000:
  value+=str(i)
  i+=1
ans = 1
for p in range(7):
  ans*=int(value[10**p-1])
print(ans)
count = 0
for i in range(1000):
  for j in range(i, 100):
    value = i**j
    if len(str(value)) == j: 
      count+=1
print(count)
num = 600851475143
i = 1
while num > 1:
  if num%i == 0: 
    num = num / i
    print(i)
  i += 1
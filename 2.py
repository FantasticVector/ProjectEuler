a = 0
b = 1
sum = 0
while b <= 4000000:
  c = b 
  b = a+b
  a = c
  if b%2 == 0: sum+=b
print(sum)

def digits(num):
  return sorted([i for i in str(num)])
for num in range(1, 1000000):
  values = digits(num)
  if all([digits(num*i) == values for i in range(1, 7)]):
    print(num)
    break
  
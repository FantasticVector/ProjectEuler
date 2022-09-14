def compute():
  values = []
  for n in range(3, 1001):
    if n%2 == 0: values.append(n*(n-2))
    else: values.append(n*(n-1))
  print(sum(values))

compute()
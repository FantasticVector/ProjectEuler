def isPlindrome(str):
  return str==str[::-1]
values = []
for i in range(1000000):
  if isPlindrome(str(i)) and isPlindrome(bin(i)[2:]):
    values.append(i)
print(values)
print(sum(values))
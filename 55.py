# Lychrel Numbers
def isLychrel(num):
  i = 0
  while i < 50:
    num = num+int(str(num)[::-1])
    if str(num) == str(num)[::-1]:
      return True
    i+=1
count = 0
for i in range(1, 10000):
  if not isLychrel(i):
    count += 1
print(count)
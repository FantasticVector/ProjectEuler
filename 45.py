def isPent(num):
  return ((1+(24*num+1)**0.5)/6)%1==0
def isHex(num):
  return ((1+(8*num+1)**0.5)/4)%1==0
for i in range(286, 100000):
  tri = i*(i+1)//2
  if isPent(tri) and isHex(tri):
    print(tri)
    break

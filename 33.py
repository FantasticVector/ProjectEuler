from fractions import Fraction
values = []
for a in range(10, 100):
  for b in range(a, 100):
    a, b = str(a), str(b)
    try:
      if (a[0] == b[0] and int(a[1])/int(b[1]) == int(a)/int(b) or a[1] == b[0] and int(a[0])/int(b[1]) == int(a)/int(b) or a[0] == b[1] and int(a[1])/int(b[0]) == int(a)/int(b) or a[1] == b[0] and int(a[0])/int(b[1]) == int(a)/int(b)) and int(a)/int(b)<1:
        values.append((a, b))
    except ZeroDivisionError:
      pass
num = 1
den = 1
for i in values:
  num*=int(i[0])
  den*=int(i[1])
print(num,den)
print(Fraction(num, den))
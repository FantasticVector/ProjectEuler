from itertools import combinations
def divisors(num):
  divs = [1]
  for i in range(2, int(num**0.5)+1):
    if num%i == 0: divs.extend([i, num//i])
  return list(set(divs))

abundant_numbers = []
for i in range(1, 28123):
  if sum(divisors(i))>i: abundant_numbers.append(i)

sums= [0]*28123
for x in range(0, len(abundant_numbers)):
  for y in range(x, len(abundant_numbers)):
    sumOfAbunNums = abundant_numbers[x] + abundant_numbers[y]
    if sumOfAbunNums < 28123:
      if sums[sumOfAbunNums] == 0: sums[sumOfAbunNums] = sumOfAbunNums

print(len(sums))
ans = 0
for i in range(1, len(sums)):
  if sums[i] == 0:
    ans+=i
print(ans)
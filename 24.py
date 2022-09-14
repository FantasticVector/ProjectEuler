from itertools import permutations
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
i = 1
for per in permutations(a):
  if i == 1000000: break
  i+=1
print(''.join(list(map(str,per))))
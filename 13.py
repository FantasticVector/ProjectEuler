from math import prod
with open("./ProjectEuler/13_input.txt") as f:
  temp = f.read().splitlines()

sum = str(sum([int(i) for i in temp]))
print(sum[:10])
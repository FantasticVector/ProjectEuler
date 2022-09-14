from math import prod
with open("./ProjectEuler/8_input.txt") as f:
  temp = f.read().splitlines()
  nums = ''.join(temp)

max_prod = 0
for i in range(len(nums)-12):
  val = prod([int(i) for i in nums[i:i+13]])
  if val > max_prod: max_prod = val

print(max_prod)
  

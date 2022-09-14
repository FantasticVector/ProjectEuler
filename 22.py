with open('./ProjectEuler/22_input.txt') as f:
  temp = f.read().replace('"', '').split(',')
  temp = sorted(temp)

def score(name):
  return sum([ord(letter) - 64 for letter in name])

value = 0
for name in temp:
  value += score(name)*(temp.index(name)+1)
print(value)
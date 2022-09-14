with open('./ProjectEuler/42_input.txt', 'r') as f:
  temp = f.read().replace('"', '').split(',')
longest_word = len(max(temp, key=len))
triangle_nums = [(n*(n+1))//2 for n in range(longest_word*26)]
count = 0
for word in temp:
  word_value = sum([ord(letter)-64 for letter in word])
  if word_value in triangle_nums: count+=1

print(count)
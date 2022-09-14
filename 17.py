from num2words import num2words
ans = [num2words(i).replace('-', '').replace(' ', '') for i in range(1, 1001)]
print(len(''.join(ans)))
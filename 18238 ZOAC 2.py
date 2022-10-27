I = input()

str = 'A' + I
sum = 0

for i in range(len(str)):
    if i+1 == len(str):
        break
    elif abs(ord(str[i])-ord(str[i+1])) > 13:
        sub = 26 - abs(ord(str[i]) - ord(str[i+1]))
        sum += sub
    else:
        sum += abs(ord(str[i]) - ord(str[i+1]))
    
print(sum)
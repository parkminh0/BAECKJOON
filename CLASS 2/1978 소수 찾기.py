N = int(input())
n = map(int, input().split())
count = 0

for i in n:
    if i == 1:
        continue
        
    test = 1
    increase = 2
    while increase <= i:
        if i % increase == 0:
            test += 1
        if test > 2:
            break
        increase += 1
        
    if test == 2:
        count += 1
    
print(count)
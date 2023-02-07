import math

M, N = map(int, input().split())

for i in range(M, N+1):
    if i == 1:
        continue
    
    sosu = True
    chk = []
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0:
            sosu = False
            break
        
    if sosu:
        print(i)
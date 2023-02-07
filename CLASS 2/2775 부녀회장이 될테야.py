T = int(input())

x = []
for i in range(T):
    k = int(input()) #층
    n = int(input()) #호
    
    x = []
    for i in range(n):
        x.append(i+1) #x = [1, 2, 3, ..., n]
        
    if k == 1:
        print(sum(x)) #1+2+3+...+n
    else:
        for i in range(k-1):
            for i in range(1, len(x)):
                x[i] += x[i-1]
        print(sum(x))
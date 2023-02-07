T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())
    if N % H == 0:
        h = str(H)
        w = (N // H)
    else:
        h = str(N % H)
        w = (N // H) + 1
    
    if w < 10:
        print(int(h+"0"+str(w)))
    else:
        print(int(h+str(w)))
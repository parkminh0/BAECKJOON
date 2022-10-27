T = int(input())
J, N = map(int, input().split())
for k in range(T):
    tmp = []
    for i in range(N):
        R, C = map(int, input().split())
        tmp.append([R, C])

    tmp1 = []
    for j in tmp:
        tmp1.append(j[0]*j[1])

    tmp1 = sorted(tmp1, reverse = True)
    
    cnt = 0
    while True:
        for i in tmp1:
            J -= i
            cnt += 1
            if J <= 0:
                break;
        break
    print(cnt)
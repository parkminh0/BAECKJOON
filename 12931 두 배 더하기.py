N = int(input())
B = list(map(int, input().split()))

A = []
for i in range(N):
    A.append(0)

cnt = 0
while True:
    chk = 0
    odd = False
    for i in B:
        if i % 2 != 0:
            odd = True
    if odd == True:
        for i in range(N):
            if B[i] % 2 == 1:
                B[i] -= 1
                cnt += 1
    else:
        for i in B:
            if i == 0:
                chk += 1
        if chk == N:
            break;
        for i in range(N):
            B[i] /= 2
        cnt += 1

print(cnt)
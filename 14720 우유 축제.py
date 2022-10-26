N = int(input())
tmp = input().split()

cnt = 0
result = 0
for i in range(N):
    if int(tmp[i]) != cnt:
        pass
    else:
        cnt += 1
        result += 1
        if cnt == 3:
            cnt = 0

print(result)
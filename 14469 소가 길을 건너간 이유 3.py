N = int(input())

tmp = []
for i in range(N):
    x, y = map(int, input().split())
    tmp.append([x, y])

tmp = sorted(tmp)
cnt = 0
for i in tmp:
    if cnt < i[0]:
        cnt = i[0] + i[1]
    elif cnt >= i[0]:
        cnt += i[1]

print(cnt)
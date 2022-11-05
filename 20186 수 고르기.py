N, K = map(int, input().split())
tmp = map(int, input().split())

tmp = sorted(tmp, reverse=True)

sum = 0
cnt = 0

for i in range(N):
    sum += tmp[i] - cnt
    K -= 1
    cnt += 1
    if K == 0:
        break
    
print(sum)
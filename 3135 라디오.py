A, B = map(int, input().split())
N = int(input())
tmp = []
for i in range(N):
    a = int(input())
    tmp.append(a)

q = []
for i in tmp:
    p = abs(i-B)
    q.append([p, i])

result = min(q)
cnt = 0
if result[0] < abs(B-A):
    A = result[1]
    cnt += 1

print(abs(B-A)+cnt)
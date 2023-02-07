from collections import deque

N, K = map(int, input().split())

tmp = deque()
for i in range(N):
    tmp.append(i+1)

check = []
count = 1
while len(check) < N:
    if count % K == 0:
        check.append(tmp[0])
        tmp.popleft()
    else:
        tmp.append(tmp.popleft())
    count += 1

result = "<"
for i in check:
    result += str(i) + ", "

result = result.rstrip(", ") + ">"
print(result)
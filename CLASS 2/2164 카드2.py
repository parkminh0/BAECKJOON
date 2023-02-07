from collections import deque

N = int(input())

result = deque()
for i in range(1, N+1):
    result.append(i)

if len(result) == 1:
    print(result[0])
else:
    while len(result) != 2:
        result.popleft()
        result.append(result.popleft())
    
    print(result[1])
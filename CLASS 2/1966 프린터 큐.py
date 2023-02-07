import sys
from collections import deque
T = int(sys.stdin.readline())

for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    priority = list(map(int, sys.stdin.readline().split()))

    doc = deque()
    for i in range(N):
        doc.append([priority[i], i])
    
    count = 0
    while doc:
        if doc[0][0] != max(doc)[0]:
            no = doc.popleft()
            doc.append(no)
        else:
            if doc[0][1] == M:
                print(count + 1)
                break
            else:
                doc.popleft()
                count += 1          
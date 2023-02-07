import sys
from collections import Counter

N = int(sys.stdin.readline())

user = []
for i in range(N):
    user.append(list(map(int, sys.stdin.readline().split())))

for i in user:
    count = 1
    for j in user:
        if i[0] < j[0] and i[1] < j[1]:
            count += 1
    print(count, end=" ")
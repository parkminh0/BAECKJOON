import sys

N = int(sys.stdin.readline())

tmp = []
for i in range(N):
    tmp.append(int(sys.stdin.readline()))

tmp.sort()

for i in tmp:
    print(i)
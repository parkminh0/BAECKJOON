import sys

N = int(input())

x = [0]*10001
for i in range(N):
    x[int(sys.stdin.readline())] += 1

for j in range(10001):
    if x[j] != 0:
        for k in range(x[j]):
            print(j)
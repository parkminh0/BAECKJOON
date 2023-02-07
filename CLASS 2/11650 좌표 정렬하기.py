N = int(input())

tmp = []
for i in range(N):
    x, y = map(int, input().split())
    tmp.append([x, y])
 
tmp = sorted(tmp, key = lambda x : (x[0], x[1]))

for x, y in tmp:
    print(x, y)
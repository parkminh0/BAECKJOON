N = int(input())

tmp = []
for i in range(N):
    x, y = map(int, input().split())
    tmp.append([x, y])
    
tmp = sorted(tmp, key = lambda x : (x[1], x[0]))

for x, y in tmp:
    print(x, y)
N = int(input())

tmp = []
for i in range(N):
    tmp.append(input())

tmp = list(set(tmp))
tmp.sort()
tmp = sorted(tmp, key = lambda x : len(x))

for i in tmp:
    print(i)
    
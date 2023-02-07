N = int(input())

tmp = []
count = 0
for i in range(N):
    x, y = input().split()
    tmp.append([int(x), y, count])
    count += 1

tmp = sorted(tmp, key = lambda x : x[2])
tmp = sorted(tmp, key = lambda x : x[0])

for i in tmp:
    print(str(i[0]) + " " + i[1])
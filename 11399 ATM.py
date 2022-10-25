N = int(input())
P = map(int, input().split())

P = sorted(P)

sum = 0
tmp = []
for j in P:
    sum += j
    tmp.append(sum)

result = 0
for k in tmp:
    result += k

print(result)
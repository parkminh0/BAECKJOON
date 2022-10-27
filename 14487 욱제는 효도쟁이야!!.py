n = int(input())
v = map(int, input().split())

v = sorted(v, reverse=True)
v.pop(0)

sum = 0
for i in v:
    sum += i

print(sum)
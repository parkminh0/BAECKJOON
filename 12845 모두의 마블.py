n = int(input())
L = map(int, input().split())
L = sorted(L, reverse = True)

sum = 0
for i in range(1, n):
    sum += L[0] + L[i]

print(sum)
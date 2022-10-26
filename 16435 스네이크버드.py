N, L = map(int, input().split())
h = map(int, input().split())

h = sorted(h)
for i in range(N):
    if L >= h[i]:
        L += 1

print(L)
n = int(input())
t = map(int, input().split())

t = sorted(t, reverse=True)

for i in range(n):
    t[i] += (i+2)
    
print(max(t))
N = int(input())
x = map(int, input().split())
x = sorted(x)

result = x[-1]
for i in range(N-1):
    result += x[i]/2

print(result)
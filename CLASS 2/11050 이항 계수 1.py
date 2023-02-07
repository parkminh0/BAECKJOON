N, K = map(int, input().split())

result = 1

if K == 0:
    print(result)
else:
    for i in range(K):
        result *= N/(i+1)
        N -= 1
    print(int(result))
N, M = map(int, input().split())
CARD = list(map(int, input().split()))

result = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            tmp = CARD[i] + CARD[j] + CARD[k]
            if tmp <= M and tmp > result:
                result = tmp                
print(result)
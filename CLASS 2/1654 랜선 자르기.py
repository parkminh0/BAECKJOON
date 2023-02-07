K, N = map(int, input().split())

ranson = []
for i in range(K):
    ranson.append(int(input()))

left = 1
right = max(ranson)

while left <= right:
    mid = (left + right) // 2
    count = 0
    for i in ranson:
        count += i // mid
    
    if count < N:
        right = mid - 1
    elif count >= N:
        left = mid + 1

print(right)
import sys
N, M = map(int, sys.stdin.readline().split())
H = list(map(int, sys.stdin.readline().split()))

left = 1
right = max(H)
while left <= right:
    mid = (left + right) // 2
    count = 0
    for i in H:
        if i > mid:
            count += i - mid
    
    if count >= M:
        left = mid + 1
    else:
        right = mid - 1
        
print(right)
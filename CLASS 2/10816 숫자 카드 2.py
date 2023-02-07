from collections import deque

N = int(input())
num1 = list(map(int, input().split()))
M = int(input())
num2 = list(map(int, input().split()))

result = {}
for i in num2:
    result[i] = 0
    
for j in num1:
    if j in result:
        result[j] += 1

for i in num2:
    print(result[i], end=" ")
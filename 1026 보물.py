N = int(input())
A = map(int, input().split())
B = map(int, input().split())

sum = 0
A = sorted(A)
B = sorted(B, reverse=True)

for i in range(N):
    sum += A[i]*B[i]
    
print(sum)#hi
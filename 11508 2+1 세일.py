N = int(input())
C = []

for i in range(N):
    c = int(input())
    C.append(c)
    
C = sorted(C, reverse=True)

sum = 0
for i in range(N):
    if i % 3 == 2:
        continue
    sum += C[i]

print(sum)
T = int(input())

devide = [300, 60, 10]
result = [0, 0, 0]

if T % 10 != 0:
    print(-1)
else:
    for i in range(3):
        if devide[i] <= T:
            result[i] += T // devide[i]
            T %= devide[i]
        print(result[i], end=" ")
T = int(input())
p = [25, 10, 5, 1]

for i in range(T):
    n = int(input())
    result = [0, 0, 0, 0]
    while n != 0:
        idx = 0
        for i in p:
            cnt = 0
            while n >= i:
                n -= i
                cnt += 1
                result[idx] += 1
            idx += 1
    for i in result:
        print(i, end=' ')
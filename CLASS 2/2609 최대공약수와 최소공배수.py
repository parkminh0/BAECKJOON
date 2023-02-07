x, y = map(int, input().split())

x, y = max(x, y), min(x, y)

# 최대공약수
big = y
while big:
    if x % big == 0 and y % big == 0:
        print(big)
        break
    else:
        big -= 1

#최소공배수
print(big * (x // big) * (y // big))
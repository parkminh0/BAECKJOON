N = int(input())

first = N // 5
result = []

while first >= 0:
    count = first
    current = N - (5*count)
    if current % 3 != 0:
        count = 0
    else:
        count += current // 3
    if count != 0:
        result.append(count)
    first -= 1

if result == []:
    print(-1)
else:
    print(min(result))
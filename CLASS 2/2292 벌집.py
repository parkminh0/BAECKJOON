N = int(input())

limit = 1
result = 1
while True:
    if limit < N:
        limit += 6*result
    else:
        print(result)
        break
    result += 1
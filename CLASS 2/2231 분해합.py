N = int(input())


if N - len(str(N))*9 <= 0:
    start = 0
else:
    start = N - len(str(N))*9

while True:
    count = 0
    for i in str(start):
        count += int(i)
    if start + count == N:
        print(start)
        break
    elif start > N:
        print(0)
        break
    start += 1
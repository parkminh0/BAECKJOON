N = int(input())
first = list(map(int, input().split()))
second = list(map(int, input().split()))

sum = 0
for i in range(N):
    sum += abs(first[i]) + abs(second[i])

print(sum)
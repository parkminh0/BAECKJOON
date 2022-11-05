tmp = []
answer = 0
for i in range(11):
    D, V = map(int, input().split())
    tmp.append([D, V])
    answer += (V * 20)

tmp = sorted(tmp)

sum = 0
for i in tmp:
    sum += i[0]
    answer += sum
print(answer)
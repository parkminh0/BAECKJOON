n = int(input())

tmp = []
want = []
for i in range(n):
    want.append(int(input()))
    
count = 2
w = 0
tmp = [1]
result = ['+']
while w != len(want):
    if tmp == [] or want[w] != tmp[-1]:
        tmp.append(count)
        count += 1
        result.append('+')
        if count >= len(want)+2:
            result = []
            print("NO")
            break
    else:
        tmp.pop()
        result.append('-')
        w += 1

if result:
    for i in result:
        print(i)
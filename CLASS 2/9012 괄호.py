N = int(input())

for i in range(N):
    tmp = input()
    count = 0
    for i in tmp:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
        if count < 0:
            break
    if count != 0:
        print("NO")
    else:
        print("YES")
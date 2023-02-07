import sys

N = int(sys.stdin.readline())

stack = []
for i in range(N):
    user = sys.stdin.readline()
    if user[:2] == "pu":
        user = user.split(" ")
        stack.append(int(user[1]))
    elif user[:2] == "po":
        if stack == []:
            print(-1)
        else:
            po = stack.pop()
            print(po)
    elif user[0] == "s":
        print(len(stack))
    elif user[0] == "e":
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)
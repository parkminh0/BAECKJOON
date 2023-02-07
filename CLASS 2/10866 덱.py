import sys
from collections import deque

stack = deque()

N = int(sys.stdin.readline())
for i in range(N):
    user = sys.stdin.readline()
    if user[:2] == "pu":
        user = user.split(" ")
        if user[0][5] == "f":
            stack.appendleft(int(user[1]))
        else:
            stack.append(int(user[1]))
    elif user[:2] == "po":
        if stack:
            if user[4] == "f":
                tmp = stack.popleft()
                print(tmp)
            else:
                tmp = stack.pop()
                print(tmp)
        else:
            print(-1)
    elif user[0] == "s":
        print(len(stack))
    elif user[0] == "e":
        if stack:
            print(0)
        else:
            print(1)
    elif user[0] == "f":
        if stack:
            print(stack[0])
        else:
            print(-1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)
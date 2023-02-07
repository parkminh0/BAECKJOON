import sys
K = int(sys.stdin.readline())

stack = [0]
for i in range(K):
    num = int(sys.stdin.readline())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))
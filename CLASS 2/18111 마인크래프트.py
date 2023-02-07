import sys
from collections import Counter

N, M, B = map(int, sys.stdin.readline().split())

board = Counter()
for i in range(N):
    board += Counter(list(map(int, sys.stdin.readline().split())))

result = 0
time = 1000000000000000
board = dict(board)
for i in range(257):
    push = 0
    pop = 0
    for key in board:
        if key <= i:
            push += (i - key) * board[key]
        else:
            pop += (key - i) * board[key]
    if B + pop < push:
        continue
    test_time = push + pop * 2
    if test_time <= time:
        result = i
        time = test_time
    
print(time, result)
#     for x in range(N):
#         for y in range(M):
#             if board[x][y] > i:
#                 pop += board[x][y] - i
#             else:
#                 push += i - board[x][y]
#     if push > pop + B:
#         continue
    
#     count = pop * 2 + push
    
#     if count <= time:
#         time = count
#         result = i

# print(time, result)
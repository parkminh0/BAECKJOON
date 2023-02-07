N, M = map(int, input().split())

board = []
for i in range(N):
    board.append(input())

result = []
for i in range(N-7):
    for j in range(M-7):
        black = 0
        white = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a + b) % 2 == 0:
                    if board[a][b] == "B":
                        black += 1
                    else:
                        white += 1
                else:
                    if board[a][b] == "W":
                        black += 1
                    else:
                        white += 1
        result.append(min(black, white))
        
print(min(result))      
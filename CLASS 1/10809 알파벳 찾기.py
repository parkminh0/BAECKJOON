tmp = input()

for i in range(97, 123):
    if chr(i) in tmp:
        print(tmp.index(chr(i)), end=" ")
    else:
        print(-1, end=" ")
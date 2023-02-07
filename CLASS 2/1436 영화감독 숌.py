N = int(input())

cnt = 0
num = 666
while cnt != N:
    for i in range(len(str(num))-2):
        if str(num)[i] == "6" and str(num)[i+1] == "6" and str(num)[i+2] == "6":
            cnt += 1
            break
    if cnt == N:
        print(num)
        break
    num += 1
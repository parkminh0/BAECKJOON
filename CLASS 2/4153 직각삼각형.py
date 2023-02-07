while True:
    x = list(map(int, input().split()))
    long = x.pop(x.index(max(x)))**2
    if long == 0:
        break
    short = 0
    for i in x:
        short += i**2
    if long == short:
        print("right")
    else:
        print("wrong")
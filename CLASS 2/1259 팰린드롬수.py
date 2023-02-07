while True:
    before = input()
    if before == "0":
        break;
    after = before[::-1]
    if int(before) == int(after):
        print("yes")
    else:
        print("no")
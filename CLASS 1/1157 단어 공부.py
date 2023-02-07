tmp = input()

tmp = tmp.upper()
chk = set(tmp)
cnt = []

for i in chk:
    cnt.append(tmp.count(i))

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(list(chk)[cnt.index(max(cnt))])
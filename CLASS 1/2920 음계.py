a = input().split()

check = a
asc = sorted(a)
dsc = sorted(a, reverse=True)

if check == asc:
    print("ascending")
elif check == dsc:
    print("descending")
else:
    print("mixed")
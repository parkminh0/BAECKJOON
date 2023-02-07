L = input()
inp = input()

r = 31
n = 0
M = 1234567891
result = 0
for i in inp:
    result += ((ord(i)-96) * (r**n))
    n += 1

if result < M:
    print(result)
else:
    print(result % M)
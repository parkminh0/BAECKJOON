n = int(input())
a = map(int, input().split())
a = sorted(a)

result = a.pop(0) + a.pop(-1)

while a != []:
    min1 = a.pop(0)
    max1 = a.pop(-1)
    if min1 + max1 <= result:
        result = min1 + max1
    
print(result)
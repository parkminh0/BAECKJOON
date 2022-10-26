n = int(input())

a = 1000-n
sum = 0
price = [500, 100, 50, 10, 5, 1]

while a != 0:
    for i in price:
        while a >= i:
            a -= i
            sum += 1

print(sum)
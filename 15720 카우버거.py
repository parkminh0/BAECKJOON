B, C, D = map(int, input().split())
N = min(B, C, D)
buger = sorted(list(map(int, input().split())), reverse=True)
side = sorted(list(map(int, input().split())), reverse=True)
beverage = sorted(list(map(int, input().split())), reverse=True)
before = sum(buger) + sum(side) + sum(beverage)
tmp = []
for i in range(N):
    price = (buger[0] + side[0] + beverage[0])*0.9
    buger.pop(0)
    side.pop(0)
    beverage.pop(0)
    tmp.append(price)


print(before)
print(int(sum(tmp) + sum(buger) + sum(side) + sum(beverage)))
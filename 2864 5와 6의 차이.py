A, B = input().split()

mina = A.replace('6', '5')
minb = B.replace('6', '5')

maxa = A.replace('5', '6')
maxb= B.replace('5', '6')
    
print(int(mina) + int(minb), int(maxa) + int(maxb))
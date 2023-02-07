import math, sys
from collections import Counter
N = int(sys.stdin.readline())

tmp = []
for i in range(N):
    tmp.append(int(sys.stdin.readline()))

tmp.sort()
print(round(sum(tmp)/len(tmp)))
print(tmp[math.floor(len(tmp)/2)]) #중앙값
if len(tmp) == 1:
    print(tmp[0])
else:
    freq = Counter(tmp).most_common(2)
    if freq[0][1] == freq[1][1]:
        print(freq[1][0])
    else:
        print(freq[0][0])
print(abs(max(tmp)-min(tmp))) #범위
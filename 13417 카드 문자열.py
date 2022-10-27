T = int(input())

output = []
for i in range(T):
    N = int(input())
    tmp = input().split()
    result = tmp[0]
    for i in range(1, N):
        if ord(tmp[i]) > ord(result[0]):
            result = result + tmp[i]
        elif ord(tmp[i]) <= ord(result[0]):
            result = tmp[i] + result
    output.append(result)
    
for i in output:
    print(i)
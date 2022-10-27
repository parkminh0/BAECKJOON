T = int(input())
for i in range(T):
    N, M = input().split()
    n = N.count('1')
    m = M.count('1')
    sub = abs(m-n)
    NN = []
    MM = []
    for i in range(len(N)):
        NN.append(N[i])
        MM.append(M[i])
        
    if n >= m:   
        for i in range(len(N)):
            if NN[i] == '1' and MM[i] == '0':
                if sub == 0:
                    break                
                NN[i] = '0'
                sub -= 1

    elif n < m:
        for i in range(len(N)):
            if sub == 0:
                break
            if NN[i] == '0' and MM[i] == '1':

                NN[i] =  '1'
                sub -= 1
                
    cnt = 0
    for i in range(len(N)):
        if NN[i] != MM[i]:
            cnt += 0.5
                    
    print(int(abs(m-n)+cnt))
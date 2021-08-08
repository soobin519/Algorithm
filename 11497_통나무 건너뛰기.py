T = int(input())

for i in range(T):
    N=int(input())
    result = [0 for i in range(N)]
    test = list(map(int,input().split()))
    test.sort()
    
    for j in range(N):
        if j %2 ==0:
            result[j//2]=test[j]
        else:
            result[N-(j//2)-1]=test[j]
    #최소 난이도 출력
    m=0
    for k in range(N-1):
        m=max(m,abs(result[k]-result[k+1]))
    print(m)
    
            

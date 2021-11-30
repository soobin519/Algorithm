import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    
    k = int(input())
    file = list(map(int, input().split()))

    #dp정의
    #d[i][j] : i부터 j까지 파일을 합치는데 드는 최소 비용 
    d=[[0 for _ in range(k)]for _ in range(k)]

    for i in range(2,k+1): #구하고자하는 파일의 길이 
        for j in range(0,k-i+1): #시작점 
            d[j][j+i-1] = min([ d[j][j+a]+d[j+a+1][j+i-1] for a in range(i-1)])+sum(file[j:j+i])


    #결과 출력
    print(d[0][k-1])
    
   

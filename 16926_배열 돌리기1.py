import sys
input = sys.stdin.readline

n,m,r  = map(int, input().split())
a=min(n,m)//2
data = [ list(map(int,input().split())) for _ in range(n)]

#r번 회전 
for k in range(r): 
    for i in range(a): #줄별로 회전시킴

        temp = data[i][i] #가장 첫번째 데이터           
                
        # 제일 윗줄 오->왼 
        for j in range(i+1,m-i):
            data[i][j-1] = data[i][j]
        # 제일 오른쪽 줄  상->하        
        for j in range(i+1,n-i):
            data[j-1][m-i-1] = data[j][m-i-1]
        # 제일 아랫줄 왼->오 
        for j in range(m-2-i,i-1,-1):
            data[n-1-i][j+1] = data[n-1-i][j]
        # 제일 왼쪽 줄 하->상    
        for j in range(n-2-i,i,-1):
            data[j+1][i] = data[j][i]     

        data[i+1][i] = temp

#결과 출력   
for row in data:
    print(*row)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

#네가지 방향 
dx = [1,-1,0,0]
dy = [0,0,1,-1]
area=[]

def dfs(a,b):
    global tmp
    tmp+=1 #면적 세기 
    d[a][b] =2 #방문 등록 
    
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if 0<=nx<n and 0<=ny<m and d[nx][ny]==1:
            dfs(nx,ny)

n,m =map(int, input().split())
d = [ list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if d[i][j] ==1:
            tmp=0
            dfs(i,j)
            area.append(tmp) #그림의 면적 저장 
            

#단, 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0이다.
if area: 
    print(len(area)) #그림 개수 
    print(max(area)) #그림 최대 면적
else:
    print(0)
    print(0)

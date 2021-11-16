import sys
sys.setrecursionlimit(50000)
input = sys.stdin.readline

area=[]
result=[]
cnt=0 #영역의 개수
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n = int(input())
for i in range(n):
    area.append(list(map(int,input().split())))

#dfs
def dfs(a,b,h):
    visited[a][b] = 1
    for i in range(4):
        xx = a + dx[i]
        yy = b + dy[i]       
        if 0 <= xx < n and 0 <= yy < n and visited[xx][yy] == 0:
            if area[xx][yy]>h:
                dfs(xx, yy,h)

for k in range(max(max(area))): #영역의 최대 높이를 범위로 함
    cnt=0 #영역의 개수 초기화
    visited = [[0]*(n) for _ in range(n)] #방문 초기화 
    for i in range(n):
        for j in range(n):
            if area[i][j]>k and visited[i][j]==0:
                cnt+=1
                dfs(i,j,k)
    result.append(cnt)
                
print(max(result))
            

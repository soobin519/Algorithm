import sys
input = sys.stdin.readline
from collections import deque

dx = [-1,0,1,0]
dy = [0,-1,0,1]

n, m = map(int,input().split())
tmap = [list(map(str,input().strip())) for _ in range(n)]
        
def bfs(i,j,time):
    queue = deque()
    queue.append([i,j,time])
    visited[i][j]=1
    
    while queue:
        x,y,time = queue.popleft()

        for a in range(4):
            nx = x+dx[a]
            ny = y+dy[a]

            if 0<=nx<n and 0<=ny<m and tmap[nx][ny]=="L": #조건 충족 
                if visited[nx][ny]==0: #방문하지 않았다면
                    queue.append([nx,ny,time+1]) #시간계산 
                    visited[nx][ny]=1
    return time

result =0
for i in range(n):
    for j in range(m):
        if tmap[i][j] =="L":
            visited = [[0]*m for _ in range(n)]
            visited[i][j]=1
            result= max(result,bfs(i,j,0)) #가장 거리가 먼 육지 두 곳을 찾기 
print(result)

import sys
input = sys.stdin.readline
from collections import deque

#네가지 방향 
dx = [1,-1,0,0]
dy = [0,0,1,-1]
area = []

def bfs(a,b):
    queue =deque()
    queue.append([a,b]) #그림의 시작 위치 
    d[a][b] =2 #방문 등록
    tmp=1 #처음 그림의 면적

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and d[nx][ny]==1:
                queue.append([nx,ny])
                d[nx][ny]=2 # 방문 등록
                tmp+=1 #그림의 면적세기
    area.append(tmp) #그림 면적 담는 list 
                
n,m =map(int, input().split())
d = [ list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if d[i][j] ==1:
            bfs(i,j)

#단, 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0이다.
if area: 
    print(len(area)) #그림 개수 
    print(max(area)) #그림 최대 면적
else:
    print(0)
    print(0)
            

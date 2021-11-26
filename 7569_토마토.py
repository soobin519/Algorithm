import sys
input = sys.stdin.readline
from collections import deque

#6가지 방향 
dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

#데이터 입력 받기 
m,n,h = map(int, input().split())
box = [[list(map(int, input().split())) for i in range(n)] for i in range(h)]

#익은 토마토가 있는 곳 저장
queue=deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k]==1:
                queue.append([i,j,k]) #h,n,m
    
def bfs():
    while queue: #queue가 빌때까지 반복함
        z,x,y = queue.popleft() #익은 토마토 위치 출력 

        #익은 토마토 주변 탐색 
        for i in range(6):
            zz = z+dz[i]
            xx = x+dx[i]
            yy = y+dy[i]

            if 0<=zz<h and 0<=xx<n and 0<=yy<m: #index가 범위 안에 있으면 
                if box[zz][xx][yy]==0: #안익은 토마토면 
                    box[zz][xx][yy]=box[z][x][y]+1 #토마토 익으면서 하루 지남 
                    queue.append([zz,xx,yy]) #새로 익은 토마토 위치 저장
bfs()

#모두 다 익었는지 확인
def check():
    day=0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if box[i][j][k]==0: #안 익은 토마토가 있으면 -1출력 후 중단 
                    return -1
                else:
                    day = max(day, box[i][j][k])
    return day-1

print(check())
               


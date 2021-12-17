import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
arr = [ list(map(int,input().split())) for _ in range(n)]

shark = 2 #현재 상어 크기
now_x, now_y = 0, 0

#상어 위치 찾기 
for i in range(n):
    for j in range(n):
        if arr[i][j] ==9:
            arr[i][j]=0 #0으로 바꿔줌 
            now_x, now_y = i, j

dx = [-1,0,1,0]
dy = [0,-1,0,1]

#최단 거리 테이블 만들기 
def bfs():
    
    visited = [ [-1]*n for _ in range(n)]
    queue = deque()
    queue.append([now_x,now_y]) 
    visited[now_x][now_y] =0
    
    while queue:
        x, y = queue.popleft()
       
        #거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기 중 가장 왼쪽에 있는 물고기를 먹는다.
        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y
            if 0<=nx<n and 0<=ny<n:#범위안에 있다면 
                if visited[nx][ny]==-1: #방문한적 없으면 
                    if arr[nx][ny]<=shark: #물고기 크기가 상어보다 작거나 같으면
                        visited[nx][ny] = visited[x][y]+1 #거리 세기 
                        queue.append([nx,ny])
    return visited

def check(visited):
    x,y =0,0
    minv = 10000001
    
    for i in range(n):
        for j in range(n):
            #도착할 수 있고 먹을 수 있는 물고기 
            if visited[i][j]!=-1 and 0<arr[i][j]<shark: #상어보다 작아야함 
                if minv > visited[i][j]:
                    x,y = i,j
                    minv = visited[i][j]
    if minv ==10000001:
        return False
    else:
        return x,y,minv
    
result = 0
eat= 0

while True:
    #가장 가까운 물고기 찾기
    value = check(bfs())

    if value ==False: #물고기가 없다면 현재까지 시간 리턴
        print(result)
        break
    else:#물고기가 있다면

        # 현재 위치, 시간을 재설정하고 물고기 먹기
        now_x, now_y = value[0], value[1]
        result += value[2]
        arr[now_x][now_y] = 0
        eat += 1

        # 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가
        # 먹은 물고기 개수가 현재 상어 크기보다 크거나 같다면
        if eat >= shark:
            shark += 1
            eat = 0

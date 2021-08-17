from collections import deque

N,M =map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

queue = deque()
queue.append((0,0)) #1,1에서 시작


while queue:
    x,y = queue.popleft()

    if x==N-1 and y==M-1: break #도착했을 경우 

    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]

        if 0<=xx<N and 0<=yy<M:
            if maze[xx][yy]==1:
                queue.append((xx,yy))
                maze[xx][yy]=maze[x][y]+1

print(maze[N-1][M-1])

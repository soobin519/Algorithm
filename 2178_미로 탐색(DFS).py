import sys
sys.setrecursionlimit(50000)

N,M =map(int, input().split())

maze = [list(map(int, input())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def dfs(n,m):
    if maze[n][m] ==1:
        for i in range(4):
            x = n+dx[i]
            y = m+dy[i]
            maze[x][y]=maze[n][m]+1
            dfs(n,m)
dfs(0,0)
print(maze[N-1][M-1])

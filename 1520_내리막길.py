import sys
input = sys.stdin.readline
sys.setrecursionlimit(30000)

m,n = map(int,input().split())
l = [ list(map(int,input().split())) for _ in range(m) ]

#visited[i][j]: l[i][j]의 위치까지 가는 내리막길의 경우의 수
visited = [ [-1 for _ in range(n)] for _ in range(m)]
#visited[0][0] = 0

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x,y):
    if x ==m-1 and y==n-1: #목표 지점 도착
        return 1

    ans=0 
    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]

        if 0<=xx<m and 0<=yy<n and l[xx][yy]<l[x][y]: #방문 가능 
            if visited[xx][yy]>=0: #방문한적이 있으면
                ans +=visited[xx][yy]
            else:
                ans+=dfs(xx,yy)
    visited[x][y]=ans
    return ans

print(dfs(0,0))

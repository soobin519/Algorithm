import sys
input = sys.stdin.readline
sys.setrecursionlimit(3000)


T = int(input())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
#dfs     
def dfs(x,y,visited):
    visited[x][y]= 1
        
    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]

        if 0<=xx<M and 0<=yy<N:
            if visited[xx][yy]==0 and land[xx][yy]==1:
                dfs(xx,yy, visited)

for i in range(T):
    M, N, K = map(int, input().split()) #가로, 세로, 개수

    land = [[0]*N for _ in range(M)]
    visited = [[0]*N for _ in range(M)]
    cnt = 0

    #배추밭 만들기 
    for i in range(K):
        a, b= map(int,input().split())
        land[a][b] = 1
        

    #dfs함수 실행
    for m in range(M):
        for n in range(N):
            if visited[m][n] ==0 and land[m][n]==1:
                dfs(m,n,visited)
                cnt+=1
    print(cnt)

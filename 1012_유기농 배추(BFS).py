import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(T):
    M, N, K = map(int, input().split()) #가로, 세로, 개수

    land = [[0]*(N) for _ in range(M)]
    queue = deque()
    cnt = 0
    
    #땅 출력 
    for i in range(K):
        a, b= map(int,input().split())
        land[a][b] = 1
        
    #방문체크: BFS
    for m in range(M):
        for n in range(N):
            if land[m][n]==1:
                queue.append((m,n))
                land[m][n]=2

                while queue:
                    x, y =queue.popleft()
                
                    for i in range(4):
                        xx = x+dx[i]
                        yy = y+dy[i]

                        if 0<=xx<M and 0<=yy<N:
                            if land[xx][yy]==1:
                                queue.append((xx,yy))
                                land[xx][yy]=2
                else: cnt+=1
    print(cnt)
                
        

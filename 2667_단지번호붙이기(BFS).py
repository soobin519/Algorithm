from collections import deque

def bfs(i,j,mapp):
    queue= deque()
    queue.append((i,j))
    home=1 #단지 내 집의 개수 
    while queue:
        x,y = queue.popleft()

        dx = [1,-1,0,0]
        dy = [0,0,1,-1]                
        for a in range(4):
            xx = x+dx[a]
            yy = y+dy[a]
                    
            if 0<=xx<N and 0<=yy<N:
                if mapp[xx][yy] == 1:
                    queue.append((xx,yy))
                    mapp[xx][yy]=2
                    home+=1
    return home

N=int(input())
mapp = [ list(map(int, input())) for _ in range(N)]
result =[]

#bfs실행
for i in range(N):
    for j in range(N):
        if mapp[i][j]==1:
            mapp[i][j]=2
            result.append(bfs(i,j,mapp))

result.sort()            
print(len(result))
for i in result:
      print(i)

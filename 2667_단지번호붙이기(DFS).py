N=int(input())
mapp = [ list(map(int, input())) for _ in range(N)]
result =[]

def dfs(x,y,home):
    mapp[x][y]=2
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]                
    for a in range(4):
        xx = x+dx[a]
        yy = y+dy[a]
                    
        if 0<=xx<N and 0<=yy<N:
            if mapp[xx][yy] == 1:
                mapp[xx][yy]=2
                home=dfs(xx,yy,home+1)
    return home

home =1
for i in range(N):
    for j in range(N):
        if mapp[i][j] == 1:

            result.append(dfs(i,j,home))
print(len(result))
for i in sorted(result): print(i)


import sys
input = sys.stdin.readline
sys.setrecursionlimit(30000)

board = [ list(map(str,input().split())) for _ in range(5)]
answer = set()

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x,y,num):
    
    if len(num)==6:  #6번 돌면          
        answer.add(num) #중복을 거르기 위해 집합 사용 
        return
        
    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]

        if 0<=xx<5 and 0<=yy<5: #범위안에 있으면 
            dfs(xx,yy,num+board[xx][yy])

#모든 좌표 탐색하며 dfs 실행 
for i in range(5):
    for j in range(5):
        dfs(i,j,board[i][j])

print(len(answer))

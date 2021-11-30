import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int, input().split())
board = [list(sys.stdin.readline().strip()) for n in range(n)]
vi = [[0 for _ in range(m)] for _ in range(n)] #*표 방문 등록 

result = []

#탐색할 방향 
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(i,j):
    queue = deque()
    cnt=1 #십자가의 크기
  
    #우선 1개자리 십자가 존재하는지 check
    for k in range(4):
        xx = dx[k]+i
        yy = dy[k]+j

        if 0<=xx<n and 0<=yy<m and board[xx][yy]=='*':
            queue.append([xx,yy,k])

        if len(queue)==4:#네 방향 모두 * 존재하면 중앙 * 방문 등록 !
            vi[i][j] = 1
 

    #십자가 주변 탐색 시작
    while len(queue)==4:#네방향 모두 존재하지 않으면 실행 중단
        for _ in range(4): #네방향 모두 탐색
            x,y,k = queue.popleft()
            vi[x][y] = 1
            #star_made +=1
            nx=x+dx[k]
            ny=y+dy[k]
        
            if 0<=nx<n and 0<=ny<m and board[nx][ny] == "*":
                queue.append([nx,ny,k]) #해당 방향에 *이 존재하면 queue에 추가 

        result.append([i+1,j+1,cnt])  #네방향 탐색후 모두 존재하면 result에 추가 
        cnt+=1 #십자가 크기 +1

#실행 - 탐색하다가 *가 존재하면 시작
star_num = 0 # *의 개수 
for i in range(n):
    for j in range(m):
        if board[i][j] == "*":
            star_num +=1
            bfs(i,j)
            
#새로 만들어진 판의 *개수 세기
star_made =0
for i in range(n):
    star_made += sum(vi[i])

#결과 출력 
if len(result)==0 or star_num!=star_made: #십자가로 만들 수 없는 경우 
    print(-1)
else:
    print(len(result))
    for i in result:
        for j in i:
            print(j, end=' ')
        print()

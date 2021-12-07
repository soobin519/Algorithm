import sys
input = sys.stdin.readline
from collections import deque

#북 동 남 서   
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#왼쪽 방향 변환 
def rotate(d):
    if d ==0: #북 -> 서 
        return 3
    elif d ==1: #동 -> 북 
        return 0
    elif d ==2: #남 -> 동 
        return 1
    else: #서 -> 남
        return 2
        
def bfs(x,y,d):
    queue =deque()
    queue.append([x,y,d])
    l[x][y]=2
    cnt = 1 #청소 완료 개수 count 

    while queue:
        a, b, d = queue.popleft()
        nd=d 

        for i in range(4):
            #왼쪽 방향 좌표
            nd=rotate(nd) 
            ax = a+dx[nd]
            by = b+dy[nd]

            #왼쪽방향이 빈칸이고 청소하지 않았다면 이동하여 청소 후 중단 (a)
            if 0<=ax<n and 0<=by<m and l[ax][by] == 0: 
                queue.append([ax,by,nd]) #이동 
                l[ax][by]=2 #청소 완료
                cnt+=1
                break

            #네 방향 모두 청소가 이미 되어있거나 벽인 경우 (c)
            elif i==3:
                if d ==0: #북
                    a+=1
                elif d==1: #동
                    b-=1
                elif d==2: #남
                    a-=1
                else: #서
                    b+=1                
                queue.append([a,b,nd])#이동

                #뒤쪽 벽(후진불가능)이면 중단 (d)
                if l[a][b] ==1:
                    return cnt
                
n,m = map(int, input().split())
r,c,d = map(int, input().split()) #0:북, 1:동, 2:남, 3:서
l = [ list(map(int, input().split())) for _ in range(n)] #1:벽, 0:빈칸

print(bfs(r,c,d))


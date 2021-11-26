import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
r1,c1, r2, c2 = map(int,input().split())

#이동할 수 있는 방향 
dr = [-2,-2,0,0,2,2]
dc = [-1,1,-2,2,-1,1]

visited = [[-1 for i in range(n)] for i in range(n)]

def bfs():
    queue = deque()
    queue.append([r1,c1]) #처음 말의 위치
    visited[r1][c1] += 1 #처음 위치 도착했을 때 +1 (초기값이 -1이므로 0으로 만들어줌) 
    
    while queue:
        x,y = queue.popleft()
        
        for i in range(6):
            rx = x+dr[i]
            cy = y+dc[i]

            if 0<=rx<n and 0<=cy<n : #말이 체스판 범위 안이면
                if visited[rx][cy] == -1 : #방문한적이 없으면 
                    visited[rx][cy]= visited[x][y]+1 #방문 표시 및 count +1
                    if rx==r2 and cy == c2: #목표 위치에 도착하면 중단하고 출력 
                        break
                    else:
                        queue.append([rx,cy]) #이동한 위치 추가 
                
bfs()
print(visited[r2][c2])

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

#나이트 이동 가능 범위
dx = [1,-1,2,2,1,-1,-2,-2]
dy = [2,2,1,-1,-2,-2,1,-1]

for i in range(n):
    l = int(input())
    x1,y1 = map(int,input().split()) #현재 좌표 
    x2,y2 = map(int,input().split()) #목적지 좌표 

    visited = [[0]*l for _ in range(l)]
    visited[x1][y1]=1
    
    queue =deque()
    queue.append([x1,y1,0])
    
    #bfs
    while queue:
        #print(queue)
        temp = queue.popleft()
        a, b = temp[0], temp[1]
        print(temp)

        if a==x2 and b==y2:
            print(temp[2])
            break
        
        for i in range(8):
            xx = dx[i]+a
            yy = dy[i]+b

            if 0<=xx<l and 0<=yy<l and visited[xx][yy]==0:
                queue.append([xx,yy,temp[2]+1])
                visited[xx][yy] =1
                
        
            
                
    
           

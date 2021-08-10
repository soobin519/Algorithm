from collections import deque
import sys
input = sys.stdin.readline

#bfs
while True:
    w,h =map(int,input().split())

    #실행 종료 조건 
    if h ==0 and w ==0: break

    #지도 구성 
    mapp = [list(map(int, input().split())) for _ in range(h)]   

    queue = deque()
    cnt=0 #섬의 개수 카운트 

    #땅 찾기
    for a in range(h):
        for b in range(w):
            if mapp[a][b] == 1: #땅이면
                queue.append((a,b))
                mapp[a][b]= 2
                
                while queue:
                    
                    x,y = queue.popleft()

                    #상, 하, 좌, 우, 대각선 모두 탐색
                    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
                    dy = [0, -1, -1, -1, 0, 1, 1, 1]
                    
                    for i in range(8):
                        xx = x+dx[i]
                        yy = y+dy[i]

                        if 0<=xx<h and 0<=yy<w:
                            if mapp[xx][yy]==1:
                                queue.append((xx,yy))
                                mapp[xx][yy]=2
                else: cnt+=1

    print(cnt)
            
    

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
k = int(input())
#사과 위치 저장 
a = [[0]*n for _ in range(n)]
for _ in range(k):
    i,j = map(int,input().split())
    a[i-1][j-1]=1
    
l = int(input())
#시간/방향 정보 저장 
info = {} 
for _ in range(l):
    i,j = map(str,input().split())
    info[int(i)]=j

#상, 우, 하, 좌
#0, 1, 2, 3
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#회전 
def rotate(d, c):
    if c =="L": #왼쪽으로
        d = (d-1)%4       
    elif c =="D":
        d = (d+1)%4
    return d
    
snake =deque() #뱀 위치 정보 담기 
time = 0
x, y  = 0,0 #시작점
direction = 1 #초기 방향 : 오 
snake.append([x,y])
a[x][y] = 2 #뱀 방문 등록 

while True:

    #앞으로 이동 
    x += dx[direction]
    y += dy[direction]
    time +=1 

    # 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다
    if 0<=x<n and 0<=y<n and a[x][y]!=2:
        snake.append([x,y]) #뱀 머리 추가

        if a[x][y]==1: #사과가 존재하면
            a[x][y]=2 #사과 먹고 이동
            
        else: #사과가 존재하지 않으면
            a[x][y]=2
            tx,ty = snake.popleft()#꼬리
            a[tx][ty] = 0 #꼬리 자르기

        if time in info.keys(): #방향변환이 존재하면
            direction = rotate(direction, info[time]) #방향 바꿔줌 
    else:
        break
print(time)
    
    

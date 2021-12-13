import sys
input = sys.stdin.readline
from collections import deque

n,k = map(int, input().split())
arr = deque(list(map(int, input().split())))

#처음엔 로봇올리고 시작인가? x
cnt =0
robot = deque([0]*n) #로봇 

while True:
    #1. 벨트가 로봇과 함께 회전 - (queue를 이용할 경우 rotate 함수 사용 가능
    arr.rotate(1)
    robot.rotate(1)
    robot[n-1]=0 #로봇 내려감 
      
    #2. 벨트가 회전하는 방향으로 로봇 한 칸 이동
    if sum(robot): #로봇이 존재하면 
        for i in range(n-2,-1,-1):
            if robot[i]==1 and robot[i+1]==0 and arr[i+1] >=1 : #다음칸이 비어있고 내구도가 0이 아니면 이동한다.
                arr[i+1]-=1
                robot[i+1]=1
                robot[i]=0
        robot[n-1]=0#로봇 내려감 
 

    #3. 로봇올리기 
    if robot[0]==0 and arr[0] >=1: #올리는 위치에 아무것도 없고 내구도가 0보다 크면,
        arr[0]-=1
        robot[0]=1 #로봇 추가 

    cnt+=1
    
    #4. 내구도가 0인 칸의 개수가 k개 이상이면 중단
    if arr.count(0) >=k:
        break

print(cnt)    
    

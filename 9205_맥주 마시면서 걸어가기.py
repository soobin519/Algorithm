import sys
input = sys.stdin.readline
from collections import deque

def bfs(x1,x2):

    queue =deque()
    queue.append([x1,y1]) #시작 좌표, 맥주 개수
    visited=[] #방문 체크 

    while queue:
        x,y = queue.popleft()
        if x == x2 and y == y2: #도착지점과 일치하면 중단 
            print("happy")
            return
        
        for i,j in location: #페스티벌 도착 좌표 포함                         
            if abs(i-x)+abs(j-y)<=1000 : #현재 가진 맥주로 도착가능하면
                if [i,j] not in visited: #방문한적이 없으면. 
                    queue.append([i,j])
                    visited.append([i,j]) #방문 등록
    print("sad")

for t in range(int(input())):

    n = int(input()) #편의점의 개수
    x1, y1 = map(int, input().split()) #집 
    location = [ list(map(int, input().split())) for _ in range(n)] #편의점 좌표  
    x2, y2 = map(int, input().split()) #페스티벌
    location.append([x2,y2])

    bfs(x1,x2)

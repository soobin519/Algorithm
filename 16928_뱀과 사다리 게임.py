import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int,input().split())
info = [0 for i in range(101)] #사다리와 뱀 정보 저장 
visited = [-1 for i in range(101)] #방문 등록 및 계산 횟수 count / count수도 세야하므로 -1로 초기화
queue = deque()

#사다리 정보 저장 
for i in range(n):
    x,y = map(int,input().split())
    info[x] = y

#뱀 정보 저장 
for i in range(m):
    u,v = map(int,input().split())
    info[u] = v
    
def bfs(start):
    queue.append(start) #시작점 queue에 등록
    visited[start] = 0 #시작점은 count 안하므로 0으로 방문 
    
    while queue:
        n= queue.popleft() #사다리 위치 출력 
        
        for i in range(1,7): #주사위 던지기
            node = n+i #주사위 수만큼 이동 

            if 1<=node<=100: #칸 범위 안에 존재하면 
                if info[node]!=0: #해당 위치에 존재하면 사다리 혹은 뱀이 존재하면
                    node=info[node] #node 사다리 또는 뱀의 영향으로 변경 
 
                if visited[node]==-1: #방문한적이 없으면 
                    queue.append(node)
                    visited[node]=visited[n]+1 #방문 등록 및 count+1

bfs(1)
print(visited[100])

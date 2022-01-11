import sys
input = sys.stdin.readline
from collections import deque

n,m,k,x = map(int,input().split())

#도시 그래프 만들기 
graph =[[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    
result =[]
dist = [0]*(n+1)
visited = [0]*(n+1)

def bfs(i): #i:시작위치 
    global result
    queue = deque()
    queue.append(i)
    dist[i]= 0 #거리 저장 
    visited[i] = 1 #방문 처리 

    while queue:
        t =queue.popleft()
        for j in graph[t]:
            if not visited[j]:
                visited[j] =True #방문체크 
                dist[j] = dist[t]+1 #거리+1
                queue.append(j)

                if dist[j] ==k: #최단거리가 k인지점 result에 추가 
                    result.append(j)
            
bfs(x)
if len(result)==0:
    print(-1)
else:
    result.sort()
    for r in result: print(r)
    

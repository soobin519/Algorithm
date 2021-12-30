import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int,input().split())
r = [[] for _ in range(n+1)]

#신뢰관계등록 
for i in range(m):
    a,b = map(int,input().split())
    r[b].append(a)

def bfs(x):
    queue = deque()
    queue.append(x)
    visited[x]=1
    
    while queue:
        x = queue.popleft()
        for i in r[x]: #해킹할 수 있는 관계이고 
            if visited[i] ==0: #아직 해킹x라면 
                queue.append(i)
                visited[i]=1

result = []
for i in range(1,n+1): #각 컴퓨터가 해킹할 수 있는 컴퓨터 개수 세기 
    visited = [0]*(n+1) #매번 초기화 필요 
    bfs(i)
    result.append(visited.count(1)) #해킹할 수 있는 개수 세서 저장 

#한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 오름차순으로 출력
max_c=max(result)
for i in range(n):
    if result[i]==max_c:
        print(i+1, end=' ')

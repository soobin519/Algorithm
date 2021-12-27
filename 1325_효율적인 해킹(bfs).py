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
        for i in r[x]:
            if visited[i] ==0:
                queue.append(i)
                visited[i]=1

result = []
for i in range(1,n+1):
    visited = [0]*(n+1)
    bfs(i)
    result.append(visited.count(1))

max_c=max(result)
for i in range(n):
    if result[i]==max_c:
        print(i+1, end=' ')

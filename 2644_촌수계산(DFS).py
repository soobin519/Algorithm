import sys
sys.setrecursionlimit(50000)
input = sys.stdin.readline

n = int(input())
a,b=map(int,input().split())
m = int(input())

family = [[] for _ in range(n+1)]
visited = [0]*(n+1)

#가족 관계 등록 
for i in range(m):
    x,y = map(int, input().split())
    family[x].append(y)
    family[y].append(x)
#print(family)

#dfs
def dfs(p):
    for i in family[p]:
        if visited[i]==0:
            visited[i]=visited[p]+1
            dfs(i)

dfs(a)
#출력
if visited[b]>0:
    print(visited[b])
else:
    print(-1)

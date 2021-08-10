import sys
input = sys.stdin.readline

n, connect = int(input()), int(input())

dic={}
for i in range(n):
    dic[i+1] = set()

for j in range(connect):
    a, b = map(int,input().split())
    dic[a].add(b)
    dic[b].add(a)

#bfs
def bfs(dic, start):
    queue = [start]
    while queue:
        for i in dic[queue.pop()]:
            if i not in visited:
                visited.append(i)
                queue.append(i)

#dfs
def dfs(dic, start):
    for i in dic[start]:
        if i not in visited:
            visited.append(i)
            dfs(dic,i)


visited = []
bfs(dic,1)
dfs(dic,1)
print(len(visited)-1)
    

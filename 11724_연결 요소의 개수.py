import sys
sys.setrecursionlimit(10**7)#재귀의 깊이를 늘려줌
input = sys.stdin.readline

N, M = map(int, input().split())

dic = [[0]*(N+1) for _ in range(N+1)]

for i in range(M):
    a, b = map(int,input().split())
    dic[a][b] = b
    dic[b][a] = a

#dfs: 깊이 우선 탐색
def dfs(dic, start):
    visited.append(start)
    for j in dic[start]:
        if j!=0 and j not in visited:
            dfs(dic, j)

visited = []
cnt=0

#dfs 실행
for i in range(1, N+1):
    if i not in visited:
        dfs(dic,i)
        cnt+=1
print(cnt)

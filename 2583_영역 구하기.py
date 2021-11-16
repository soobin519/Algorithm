import sys
sys.setrecursionlimit(50000)
input = sys.stdin.readline

x,y,k = map(int, input().split())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
visited = [[0]*(y) for _ in range(x)]
cnt = 0 #영역 개수
area = 1 #넓이
ans=[]

#dfs     
def dfs(a,b):
    global area
    visited[a][b] = 1
    for i in range(4):
        xx = a + dx[i]
        yy = b + dy[i]
        if 0 <= xx < x and 0 <= yy < y and visited[xx][yy] == 0:
            area += 1
            dfs(xx, yy)


for o in range(k): #방문 등록 
    y1,x1,y2,x2 = map(int, input().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            visited[i][j]=1

for i in range(x):
    for j in range(y):
        if visited[i][j] == 0:
            cnt += 1
            dfs(i, j)
            ans.append(area)
            area = 1 #넓이 초기화

ans.sort()
print(cnt)
print(' '.join(map(str, ans)))

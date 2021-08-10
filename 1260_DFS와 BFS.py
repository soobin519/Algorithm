from collections import deque

N, M, V = map(int,input().split())

dic = [[0]*(N+1) for i in range(N+1)]
visited = []

#그래프로 만들기 
for i in range(M):
    a, b = map(int, input().split())
    dic[a][b]=b
    dic[b][a]=a

#dfs
def dfs(dic, start):
    visited.append(start)
    print(start, end=' ')
    for i in dic[start]:
        if i !=0 and i not in visited:
            dfs(dic,i)
            
#bfs
def bfs(dic, start):
    #리스트를 써서 pop(0)하면 시간복잡도가 O(N). 그래서 시간복잡도가 O(1)인 deque를 사용.
    queue = deque()
    queue.append(start)
    visited =[start]

    while queue: #끊어진 부분을 위해 while문을 꼭 넣어줘야함!!
        a = queue.popleft()
        print(a, end =' ')
        for i in dic[a]:
            if i !=0 and i not in visited:
                visited.append(i)
                queue.append(i)
dfs(dic,V)
print()
bfs(dic,V)

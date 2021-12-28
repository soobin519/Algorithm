import sys
input = sys.stdin.readline

n= int(input())
p=list(map(int, input().split()))
x =int(input())

#트리 그래프 만들기
root=-1
node =[[] for _ in range(n)]
for i in range(n):
    if p[i]!=-1:
        node[p[i]].append(i)
    else: #루트일경우
        root = i      
#print(node)

#리프노드 개수 구하기 
def dfs(r): #매개변수 root
    global cnt
    if len(node[r])==0: #자식노드x, 리프노드라면
        cnt+=1
    else: #아닐 경우 이어진 자식노드 탐색 
        for i in node[r]:
            dfs(i)

#제거해야할 노드 먼저 제거 
for i in range(n):
    if x in node[i]:
        node[i].remove(x)
#print(node)

cnt=0
if x!=root:
    dfs(root) #리프노드 탐색 
print(cnt)



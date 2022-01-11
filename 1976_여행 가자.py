import sys
input = sys.stdin.readline

#유니온 파인드(합집합 찾기) = 서로소 찾기   

#부모 노드를 찾는 함수 
def getParent(parent, x):
    if parent[x] != x:
        parent[x] = getParent(parent, parent[x])
    return parent[x]

#두 부모 노드를 합치는 함수  
def unionParent(parent, a, b):
    a = getParent(parent,a)
    b = getParent(parent,b)
    if a<b:
        parent[b]=a
    elif a>b:
        parent[a]=b
    else:
        return

n =int(input())
m =int(input())

#부모노드 임의 저장 
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

for i in range(1,n+1):
    arr = list(map(int,input().split()))
    for j in range(1,n+1):
        if arr[j-1] ==1:
            unionParent(parent,i,j)

plan = list(map(int,input().split()))
result = []
for i in plan:
    result.append(getParent(parent,i))

if len(set(result)) == 1:
    print("YES")
else:
    print("NO")

    

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n=int(input())
tree=[[] for i in range(n+1)]

#트리만들기 
for i in range(n-1):
    p,c,w = map(int,input().split())
    tree[p].append([c,w])
print(tree)

max_n=0
def dfs(node,result):
    left,right = 0,0
    
    for newNode, weight in tree[node]:
        print(left,right)
        r = dfs(newNode,weight)
        print("r",r)
        if left<=right:
            left = max(left,r)
            print(left,"left")
        else: #right<left
            right=max(right,r)
            print(right,"right")
        
    global max_n
    max_n = max(max_n,left+right)
    return max(left+result,right+result) #가중치 반환
dfs(1,0)
print(max_n)

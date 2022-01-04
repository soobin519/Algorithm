import sys
input = sys.stdin.readline

n = int(input())

#트리만들기
tree = {}
for i in range(n):
    root, l,r = map(str,input().split())
    tree[root]=[l,r]

def preorder(node): #루트->왼->오
    if node == ".":
        return
    print(node,end="")
    preorder(tree[node][0]) #왼
    preorder(tree[node][1]) #오

def inorder(node): #왼->루트->오
    if node == ".":
        return
    inorder(tree[node][0]) #왼
    print(node,end="")
    inorder(tree[node][1]) #오

def postorder(node): #왼->오->루트
    if node == ".":
        return
    postorder(tree[node][0]) #왼
    postorder(tree[node][1]) #오
    print(node,end="")
    
preorder('A')
print()
inorder('A')
print()
postorder('A')

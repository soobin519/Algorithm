import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

num=[]
while True:
    try:
        num.append(int(input()))
    except:
        break
#print(num)

#l->r->root
def pre_to_post(tree): #후위순위
    if len(tree)<=1:
        return tree
    
    for i in range(1,len(tree)):
        if tree[0]<tree[i]: #오른쪽 노드임(오른쪽노드는 루트보다 커야함) 
            return pre_to_post(tree[1:i])+pre_to_post(tree[i:])+[tree[0]]

    return pre_to_post(tree[1:])+[tree[0]]

post=pre_to_post(num)
#print(post)
for i in range(len(post)):
    print(post[i])
        

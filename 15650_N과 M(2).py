import sys
input=sys.stdin.readline

N,M=map(int, input().split())
s=[]

def dfs():
    if len(s)==M:
        print(' '.join(map(str,s)))
        return
    i=1
    for i in range(i,N):
        if i not in s:
            s.append(i)
            print(s)
            dfs()
            s.pop()
            print(s)
            print("-----")
dfs()

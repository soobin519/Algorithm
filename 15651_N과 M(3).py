import sys
input = sys.stdin.readline

N,M = map(int, input().split())
s=[]

def sol():
    if len(s)==M:
        print(' '.join(map(str,s)))
        return
    for i in range(1,N+1):
        s.append(i)
        sol()
        s.pop()
sol()

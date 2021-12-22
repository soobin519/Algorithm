import sys
input = sys.stdin.readline
from collections import deque
from itertools import permutations as pm

n = int(input())
scv = list(map(int,input().split()))
d = [[[-1]*69 for _ in range(61)] for _ in range(61)]

mu = list(pm([9,3,1])) #공격할 수 있는 가짓수


def func(a,b,c):
    if a<0:
        return func(0,b,c)
    if b<0:
        return func(a,0,c)
    if c<0:
        return func(a,b,0)

    if a==0 and b==0 and c==0:
        return 0
    if d[a][b][c] !=-1:
        return d[a][b][c]
    
    d[a][b][c]=999999
    for x in mu:
        d[a][b][c]=min(d[a][b][c], func(a-x[0], b-x[1],c-x[2]))
    d[a][b][c]+=1
    return d[a][b][c]

        
l = [0, 0, 0]
for i in range(len(scv)):
    l[i] = scv[i]
print(func(l[0], l[1], l[2]))
    
    

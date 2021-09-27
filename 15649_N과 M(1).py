#백트래킹
#- 보통 재귀로 구현하며 조건이 맞지 않으면 종료한다.
#- DFS(깊이 우선 탐색) 기반

import sys
input=sys.stdin.readline

N,M=map(int, input().split())
s=[]

def dfs():
    if len(s)==M:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,N+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()

dfs()

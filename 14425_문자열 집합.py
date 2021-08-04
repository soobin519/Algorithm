import sys
input = sys.stdin.readline

N, M = map(int, input().split())
n= set()
cnt=0
for i in range(N):
    n.add(input())
    
for i in range(N,N+M):
    m=input()
    if m in n:
        cnt+=1
print(cnt)


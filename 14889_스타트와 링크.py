import sys
input = sys.stdin.readline

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

from itertools import combinations as cb
sub =[]
for k in list(cb([i for i in range(N)],N//2)):
    n = set(range(N))-set(k) #나머지 선택
    n=list(n)
    sums=0
    for m in range(N//2-1):
        for l in range(m+1,N//2):
            sums+=(S[k[m]][k[l]]+S[k[l]][k[m]]-S[n[m]][n[l]]-S[n[l]][n[m]])
    sub.append(abs(sums))
print(min(sub))



import sys
input = sys.stdin.readline
from itertools import combinations as cb

n = int(input())
arr = [ list(map(int,input().split())) for _ in range(n)]
result =[]

#두 팀의 인원수는 같지 않아도 되지만, 한 명 이상이어야 한다.
for j in range(1,n):
    for k in list(cb([i for i in range(n)], j)):
        #팀나누기 
        start = list(k)
        link = list(set(range(n))-set(k))

        #start팀 능력치 구하기 
        sums=0
        for s1 in range(len(start)):
            for s2 in range(s1+1, len(start)):
                sums+=(arr[start[s1]][start[s2]]+arr[start[s2]][start[s1]])

        #링크팀 능력치 구하기 
        suml=0
        for l1 in range(len(link)):
            for l2 in range(l1+1, len(link)):
                suml+=(arr[link[l1]][link[l2]]+arr[link[l2]][link[l1]])

        result.append(abs(sums-suml))

print(min(result))

import sys
input = sys.stdin.readline

n = int(input())
line = [ list(map(int,input().split())) for _ in range(n)]
line.sort()

#왼쪽을 정렬했을때, 오른쪽도 정렬시키면 겹치는걸 찾을 수 있음. 
d = [1]*n

for i in range(1,n):
    for j in range(i):
        if line[j][1]<line[i][1]:
            d[i]=max(d[j]+1, d[i])
print(n-max(d))

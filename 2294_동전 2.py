import sys
input = sys.stdin.readline

n,k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
coin.sort(reverse=True) #내림차순으로 정렬 
d=[100001 for i in range(k+1)] #index의 합이 되는 경우의 수
d[0]=0

for i in coin:
    for j in range(i,k+1):
        if d[j-i]!=100001:
            d[j]=min(d[j],d[j-i]+1)
            
if d[k]!=100001:
    print(d[k])
else:
    print(-1)

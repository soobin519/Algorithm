import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coin = []

for i in range(N):
    coin.append(int(input()))
coin.sort(reverse=True)

cnt=0
#그리디 알고리즘 
for c in coin:
    cnt+=K//c
    K=K%c

print(cnt)

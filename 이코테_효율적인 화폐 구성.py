N, M = map(int, input().split())
d = [-1]*(M+1)
money = []
for i in rang e(N):
    money.append(int(input()))

d[0]=0
for i in range(N):
    for j in range(money[i], M+1):
        if d[j-money[i]]!=-1 :
            d[j] = min(d[j],d[j-array[i]+1)

if d[M]==-1: print(-1)
else: print(d[M])

N = int(input())
P = list(map(int,input().split()))
time=[0 for i in range(N+1)]
P.sort()

for i in range(1,len(P)+1):
    time[i]=time[i-1]+P[i-1]
print(sum(time))

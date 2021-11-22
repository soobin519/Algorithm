import sys
input = sys.stdin.readline
cost=[]

n = int(input())
for i in range(n):    
    cost.append(list(map(int,input().split())))

for i in range(1,n):
    #빨강 
    cost[i][0] = cost[i][0]+min(cost[i-1][1], cost[i-1][2])
    #초록  
    cost[i][1] = cost[i][1]+min(cost[i-1][0], cost[i-1][2])
    #파랑  
    cost[i][2] = cost[i][2]+min(cost[i-1][0], cost[i-1][1])

print(min(cost[n-1]))

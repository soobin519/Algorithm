#입력값 저장하기  
import sys
n=int(sys.stdin.readline())
days, cost = [], []
for i in range(n):
    d, c = map(int, sys.stdin.readline().split())
    days.append(d)
    cost.append(c)
    
#Dynamic Programming: 메모리 효율을 위해 계산한 값을 저장할 것.
result=[0 for i in range(n+1)]

for i in range(n-1,-1,-1):
    if days[i]+i<=n: #날짜를 초과하지 않을 경우
        result[i]=max(cost[i]+result[i+days[i]],result[i+1]) 
    else: #날짜를 초과할 경우
        result[i]=result[i+1]
print(result[0])

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

#i번째 좌석에서 앉을 수 있는 방법의 가짓수
#피보나치 원리 이용 
d= [ 1 for _ in range(n+1)] #0으로 초기화 하면 안됨 : 반례 4 2 1 4
d[1]=1
d[2]=2
for i in range(3,n+1):
    d[i]=d[i-1]+d[i-2]

result=1
pre = 0

for i in range(m):
    tmp=int(input())#vip    
    result *= d[tmp-pre-1] #곱의법칙 
    pre = tmp                
result*=d[n-pre] #마지막 

print(result)

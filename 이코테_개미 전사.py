import sys
input = sys.stdin.readline

n = int(input())
store=list(map(int, input().split()))

#dp 테이블 초기화
d=[0]*100

#다이나믹 프로그래밍(보톰업)
d[0]=store[0]
d[1]=max(store[0],store[1])

for i in range(2,n):
    d[i]=max(d[i-1], d[i-2]+store[i])

print(d[n-1])

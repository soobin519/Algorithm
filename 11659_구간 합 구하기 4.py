import sys
input =sys.stdin.readline

n,m=map(int,input().split())
arr = list(map(int,input().split()))

#dp정의 
d = [0]
for i in range(1,n+1):
    d.append(d[i-1]+arr[i-1])

#구간합구하기 
for _ in range(m):
    i,j = map(int,input().split())

    print(d[j]-d[i-1])

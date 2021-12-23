import sys
input  = sys.stdin.readline

#dp정의
d = [0]*(1000000+1)
for i in range(1,1000000+1):
    if i==1:
        d[1]=1
    elif i==2:
        d[2]=2
    elif i==3:
        d[3]=4
    else:
        d[i] = (d[i-1]+d[i-2]+d[i-3])%1000000009
        
for t in range(int(input())):
    n = int(input())
    print(d[n])

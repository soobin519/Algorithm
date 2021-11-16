import sys
input = sys.stdin.readline

n,k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
d=[0 for i in range(k+1)] #index의 합이 되는 경우의 수 

for i in coin:
    for j in range(i,k+1):
        if j<i: d[j]+=0
        elif i==j:d[j]+=1      
        else:
            d[j]+=d[j-i]
    
print(d[k])

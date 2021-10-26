import sys
input = sys.stdin.readline

n = int(input())
d=[0]*11
#초기값 
d[1]=1
d[2]=2
d[3]=4

for i in range(4,11):
    d[i]=d[i-1]+d[i-2]+d[i-3]
for j in range(n):
    a=int(input())
    print(d[a])
    
    

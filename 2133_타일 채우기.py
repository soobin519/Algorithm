import sys
input = sys.stdin.readline

n = int(input())

#dp정의 : 해당 index까지 도달했을때 만들   수 있는 경우의 수
d = [0]*(n+1)

for i in range(n+1):
    if i==0:
        d[i]=1
    elif i==2:
        d[i]=3
    elif i%2==0:
        d[i]= d[i-2]*3
        for j in range(4,i+1,2): 
            d[i]+=d[i-j]*2
print(d[n])
            
    
 

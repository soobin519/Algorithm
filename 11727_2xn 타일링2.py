import sys
input = sys.stdin.readline

n = int(input())

#dp정의 : 해당 index까지 도달했을때 만들 수 있는 경우의 수
#d[n] = d[n-1]+d[n-2]*2
d = [0]*(n+1)

for i in range(1,n+1):
        if i ==1:
                d[i]=1
        elif i ==2:
                d[i]=3
        else:
                d[i]= d[i-1]+d[i-2]*2
print(d[n]%10007)



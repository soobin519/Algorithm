import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int,input().split()))

#dp정의
d = [0]*n
max_n = num[0] #처음 값으로 Max값 임의 설정

for i in range(n):   
    if i ==0:
        d[0] =num[0]
    else:
        d[i] = max(d[i-1]+num[i],num[i])

    if max_n<d[i]:
        max_n=d[i]
        
print(max_n)

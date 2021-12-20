import sys
input = sys.stdin.readline

n= int(input())

#dp정의 - d[0],d[1]=1 (첫자리는 무조건 1, 두번째자리는 무조건 0) 1가지씩
d = [1]*n

for i in range(n):
    if i==0:
       d[i]=1
    elif i ==1: 
       d[i]=1      
    else:
        d[i]=d[i-1]+d[i-2]

print(d[n-1])

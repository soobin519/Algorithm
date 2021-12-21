import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

#dp정의 
#d = a
d = [ i for i in a]

for i in range(1,n):
    for j in range(i):
        if a[j]<a[i]:
            d[i] = max(d[j]+a[i],d[i])

print(max(d))

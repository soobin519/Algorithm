import sys
input = sys.stdin.readline

a = int(input())
arr = list(map(int, input().split()))

d = [1]*(a)

for i in range(1,a):
    for j in range(i):
        if arr[i]>arr[j]:
            d[i] = max(d[i],d[j]+1)

print(max(d))

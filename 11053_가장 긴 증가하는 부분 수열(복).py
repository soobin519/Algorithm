import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))

#dp: i번째까지 증가했을떼 수열의 최대 길이 
d = [1]*n

for i in range(1,n):
    for j in range(i):
        if a[j]<a[i]:
            d[i] = max(d[j]+1,d[i])
print(max(d))

import sys
input = sys.stdin.readline

n = int(input())
box = list(map(int, input().split()))

#dp: i번째까지 넣었을 때 최대 박스의 개수 
d = [1]*(n)

for i in range(1,n):    
    for j in range(i):
        if box[i]>box[j]:
            d[i] = max(d[i],d[j]+1)
print(max(d))

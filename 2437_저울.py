import sys
input = sys.stdin.readline

n = int(input())
lis= list(map(int,input().split()))
lis.sort()

tmp =1
for i in lis:
    if tmp<i:
        break
    tmp+=i

print(tmp)

import sys
input = sys.stdin.readline

N, L = map(int, input().split())
leak = list(map(int,input().split()))
leak.sort()

cnt=0
start=0

for i in leak:
    if start<i:
        start=i+L-1
        cnt+=1
    
print(cnt)
        
    
    

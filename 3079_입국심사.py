import sys
input = sys.stdin.readline

n, m = map(int,input().split())
time = [int(input()) for _ in range(n)]

result = 0    
start = 0
end = (max(time))*m

while start<=end:
    mid = (start+end)//2
    
    cnt = 0
    for x in time:
        cnt+=(mid//x)


    if cnt<m:
        start = mid+1 
    else:
        result=mid
        end= mid-1 
                  


print(result)

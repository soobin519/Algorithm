import sys
input = sys.stdin.readline

n,m = map(int, input().split())
h = list(map(int,  input().split()))

start = 0
end = max(h)

#이진 탐색
result = 0
while(start<=end):
    total = 0
    mid = (start+end)//2

    #떡을 잘랐을 때 높이 합 계산 
    for x in h:
        if x>mid:
            total+= x-mid

    #떡이 부족한 경우, 
    if total<m:
        end = mid-1
    #떡이 충분한 경우 
    else:
        result = mid
        start=mid+1
print(result)
        

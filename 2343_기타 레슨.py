import sys
input = sys.stdin.readline

n,m = map(int, input().split())
lec = list(map(int, input().split()))

start =max(lec) #최소 한개의 강의는 들어야하므로 
end = sum(lec)
result = 1000001

#이분탐색 실행 
while start<=end :
    mid = (start+end)//2    
    total =0
    i=0 #블루레이 개수
    
    for x in lec:
        if total+x>mid:
            i+=1
            total=0
        total += x

    #마지막 블루레이 개수 추가
    if total:
        i+=1

    #사용한 블루레이 개수를 초과하지 않은 경우(한 블루레이에 너무 많은 강의가 배정된 경우)
    if i<=m:
        end = mid-1
        result = min(result,mid)
    #사용한 블루레이 개수를 초과한 경우,강의 수용을 늘려야하므로 
    else:
        start= mid+1

print(result)
        

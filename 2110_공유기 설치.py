import sys
input = sys.stdin.readline

n,c = map(int,input().split())
home = [ int(input()) for _ in range(n)]
home.sort()

#두 공유기의 거리 
start = 1
end = max(home)-min(home)

#이분탐색 
while start<=end:
    mid = (start+end)//2
    #print("mid", mid)

    #두 공유기 사이의 거리를 mid로 정했을 때 설치 가능한 공유기의 개수
    cnt =1
    now = home[0]
    
    for i in range(1,n):
        if abs(home[i]-now)>=mid:
            cnt+=1
            now = home[i]
            
    #print(cnt)
    if cnt>=c: #설치한 공유기가 원래 개수보다 많으면
        start = mid+1
        ans=mid #정답 가능성이 있으므로 정답에 넣어준다.
    else:
        end = mid -1

print(ans)
        

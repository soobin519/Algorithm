import sys
input = sys.stdin.readline

k,n = map(int,input().split())
lis = [int(input()) for _ in range(k)]
lis.sort()

def search():
    start = 1
    end = lis[-1]
    ans = []

    while start<=end:
        mid = (start+end)//2
        cnt = 0
        for i in range(k):
            cnt+=lis[i]//mid

        if cnt<n:
            end = mid-1
        else: #if cnt>=n:
            start = mid+1
            ans.append(mid)
    return max(ans)

print(search())
    

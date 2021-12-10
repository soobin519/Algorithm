import sys
input = sys.stdin.readline

#이분 탐색 
def search(a,x):
    start =0
    end = n-1
    
    while start<=end:
        mid = (start+end)//2
        if x==a[mid]:
            return 1
        elif x>a[mid]:
            start=mid+1
        elif x<a[mid]:
            end=mid-1

    return 0

n = int(input())
a = list(map(int,input().split()))
a.sort()

m = int(input())
a2 = list(map(int,input().split()))

for k in a2:
    print(search(a,k))

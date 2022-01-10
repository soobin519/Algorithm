import sys
input = sys.stdin.readline

#반례
#5 11
#1 5 2 1 4 3 2 1 2 1 3
#11

h,w = map(int,input().split())
height = list(map(int,input().split()))
total = 0

for i in range(1,w-1):
    left_h = max(height[:i]) #왼쪽 기둥 최대값 
    right_h = max(height[i+1:]) #오른쪽 기둥 최대값

    now_h = min(left_h, right_h)
    
    if height[i]<now_h:
        total+=(now_h - height[i])
                  
print(total)

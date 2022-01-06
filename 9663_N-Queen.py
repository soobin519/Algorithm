import sys
input = sys.stdin.readline

n = int(input())
#퀸은 일직선으로 앞, 뒤, 옆, 대각선 어떤 방향이든 원하는 만큼 이동가능

check1 =[True]*n #열확인 
check2 =[True]*(n*2-1) #대각선확인 (x+y)
check3 =[True]*(n*2-1) #대각선확인 (x-y)
cnt=0

def func(num):
    global cnt
    
    if num ==n:#퀸을 모두 체스판에 놓았으면 cnt+=1
        cnt+=1
        return

    for i in range(n):
        if check1[i] and check2[i+num] and check3[num-i+n-1]: #모두 조건을 만족하면
            check1[i]=False
            check2[i+num]=False
            check3[num-i+n-1]=False
            func(num+1)
            check1[i]=True
            check2[i+num]=True
            check3[num-i+n-1]=True
func(0)
print(cnt)

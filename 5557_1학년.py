import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int,input().split()))

#d[i][j]: i번째 연산에서 j를 만들 수 있는 경우의 수 
d = [[0]*21 for i in range(n-1)]
d[0][num[0]] =1 #첫번째 수 

for i in range(1,n-1):
    for j in range(21):
        if d[i-1][j]!=0:
            tmp1 = j+num[i]
            tmp2 = j-num[i]

            if 0<=tmp1<=20:
                d[i][tmp1]+=d[i-1][j]
            if 0<=tmp2<=20:
                d[i][tmp2]+=d[i-1][j]   
    
print(d[n-2][num[-1]]) #결과 출력 

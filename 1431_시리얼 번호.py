import sys
input = sys.stdin.readline

N = int(input())

num = [[0]*2  for i in range(N)]
s=''

for i in range(N):
    s=input().rstrip()
    a=0
    for j in s:
        if j.isdigit() ==True:
            a+=int(j)
    num[i][0]=s #입력된 시리얼 번호 
    num[i][1]=a #숫자합
    
num.sort(key=lambda x: (len(x[0]),x[1],x[0]))

for i in range(N):
    print(num[i][0])

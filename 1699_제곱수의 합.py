import sys
input = sys.stdin.readline

n= int(input())

#dp테이블 초기화
#dp : i가 되었을 때 제곱수 항의 개수의 최솟값. 
d = [i for i in range(n+1)]

for i in range(1,n+1):
    for j in range(1,i): 
        if j*j>i: #제곱수가 i보다 크면 중단 
            break

        if d[i] > d[i-j*j]+1: #최솟값을 발견하면 d[i]갱신 
            d[i] = d[i-j*j]+1

print(d[n])

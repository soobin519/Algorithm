import sys
input = sys.stdin.readline

n= int(input())

#dp테이플 초기화 - dp테이블에 연산 횟수를 담는다. 
d=[0]*(n+1)
for i in range(2, n+1):
    # 1을 빼고 시작하는 이유는 다음에 계산할 나누기가 1을 뺀 값보다 작거나 큼에 따라 어차피 교체되기 때문
        d[i]=d[i-1]+1

        if i%2==0:
            d[i]=min(d[i],d[i//2]+1)
        if i%3==0:
            d[i]=min(d[i],d[i//3]+1)

print(d[n])
    
 

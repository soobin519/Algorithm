n = int(input())
d = [0]*(n+1) #연산횟수 저장  

#다이나믹 프로그래밍 진행(보텀업) 
for i in range(2, n+1):
    #우선 1을 빼고 시작
    #+1 은 연산 횟수 추가 
    d[i] = d[i-1]+1

    if i%2 ==0:
        d[i]=min(d[i],d[i//2]+1)
    if i%3 ==0:
        d[i]=min(d[i],d[i//3]+1)

print(d[n])
 

n = int(input())
time =[[0]*2 for i in range(n)]

for i in range(n):
    b,e = map(int, input().split())
    time[i][0] = b
    time[i][1] = e

time.sort(key=lambda x:(x[1],x[0])) #소요시간 적은 순서대로 정렬  

cnt =1
t =time[0][1] 
for i in range(1,n):
    if time[i][0]>= t:
        cnt+=1
        t =time[i][1]
        
print(cnt)



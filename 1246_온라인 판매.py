import sys
input = sys.stdin.readline

n,m  = map(int,input().split())
p =[ int(input()) for _ in range(m)] #고객이 원하는 가격
p.sort()

#두개 이상 팔지 x/(물론 달걀 총 수량을 초과하여 팔 수 는 없다 -> 달갈계수만큼만 수익 
result=[]
for k in p:
    cnt = 0
    price = k
    for i in range(m):
        if price<=p[i]: #고객이 만족하는 가격이면
            cnt+=1
    if cnt<n:
        result.append([price*cnt,price])
    else:
        result.append([price*n,price])

print(max(result)[1], max(result)[0])

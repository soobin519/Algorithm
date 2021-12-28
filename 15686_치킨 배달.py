import sys
input  = sys.stdin.readline
from itertools import combinations as cb

n,m = map(int,input().split())
cmap = [list(map(int,input().split())) for _ in range(n)]


#집, 치킨집 위치 등록 
home,chicken=[], []
for i in range(n):
    for j in range(n):
        if cmap[i][j] ==1:
            home.append([i,j])
        elif cmap[i][j] == 2:
            chicken.append([i,j])

result=[]
for c in cb(chicken,m):
    mind=0
    for h in home:
        distance = []
        for x in c:
            distance.append(abs(x[0]-h[0])+abs(x[1]-h[1])) #치킨집과 집 사이의 거리 
        mind+=min(distance) #한 집과 뽑은 치킨 집들 중 최소 거리인 것을 골라 더해준다. (도시의 치킨 거리 구하기)
    result.append(mind) #구한 도시의 치킨 거리를 result리스트에 추가 
print(min(result)) #구한 도시의 치킨 거리들 중 최소값 출력 

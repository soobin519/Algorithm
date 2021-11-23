import sys
input = sys.stdin.readline

size = []
n = int(input())
for i in range(n):    
    size.append(list(map(int,input().split())))

max_l = max(size, key=lambda x: x[0])[0]# 가장 큰 L    
max_hl = max(size, key=lambda x: x[1])[0]# 가장 큰 H의 L

#기둥 정보 저장 
pillar = [0]*(max_l+1)
for l, h in size:
    pillar[l]=h

result=0 #면적
#처음부터 가장 높은 기둥까지의 면적  
temp_h=0
for i in range(max_hl+1):
    if pillar[i]>temp_h: #더 높은 높이가 나타나면 높이 갱신 
        temp_h = pillar[i]
    result+= temp_h*1

#마지막부터 가장 높은 기둥 전까지의 면적  
temp_h=0
for i in range(max_l,max_hl,-1):
    if pillar[i]>temp_h: #더 높은 높이가 나타나면 높이 갱신 
        temp_h = pillar[i]
    result+= temp_h*1

print(result)
    
    

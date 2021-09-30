import sys
input = sys.stdin.readline

n =int(input())

info=[]

for i in range(n):
    info.append(list(map(int, input().split())))

for i in info:
    rank=1
    for j in info:
        if i[0]<j[0] and i[1]<j[1]: rank+=1
    print(rank, end=" ")

        
    

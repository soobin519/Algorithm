import sys
input = sys.stdin.readline

n,m = int(input()), int(input())
r = [list(map(int, input().split())) for _ in range(m)]
friends = [[] for _ in range(n+1)] 
result=[]

for i,j in r: #친구관계 등록 
    friends[i].append(j)
    friends[j].append(i)    

for i in friends[1]: #초대할 친구 찾기 
    result.append(i)
    for j in friends[i]:
        result.append(j)
            
if len(set(result))!=0:
    print(len(set(result))-1)
else:
    print(0)

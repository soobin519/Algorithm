import sys
input = sys.stdin.readline
from collections import deque

s = int(input()) 

#d[i][j]: 화면에 있는 이모티콘의 갯수 i개, 클립보드에 있는 이모티콘의 갯수j
d = [[-1]*(s+1) for _ in range(s+1)]

queue = deque()
queue.append([1,0]) #현재 이모티콘 개수, 클립보드의 이모티콘 개수
d[1][0] = 0

while queue:
    e, tmp = queue.popleft()

    if e==s: #이모티콘 만들기 완료하면
        break

    #1. 복사 
    if d[e][e] == -1:
        d[e][e] = d[e][tmp]+1
        queue.append([e,e])

    #2.붙여넣기
    if e+tmp <= s and  d[e+tmp][tmp]==-1: #붙여넣었을때 s를 넘지 않고,  방문x
        d[e+tmp][tmp]=d[e][tmp]+1
        queue.append([e+tmp,tmp])

    #3. 삭제
    if  e-1>=0 and d[e-1][tmp]==-1:#삭제시 이모티콘 개수가 0개 이상이고 , 방문 x, 방문 x
        d[e-1][tmp] =d[e][tmp]+1
        queue.append([e-1,tmp])

#정답 찾기 
result = []   
for a in d[s]:
    if a != -1:
        result.append(a)
print(min(result))
        
    
        

        
        
        
    
    

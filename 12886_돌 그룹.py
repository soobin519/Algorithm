import sys
input = sys.stdin.readline
from collections import deque

def func(a,b,c):
    
    if (a+b+c)%3 != 0: #세 수의 합이 3으로 나누어 떨어지지 않으면 return o
        return 0
    
    queue = deque()
    queue.append([a,b,c])
    
    while queue:
        x,y,z=queue.popleft()


        if x==y==z: #세 수가 같아지면 실행중단 
            return 1
        
        if x != y:
            if x>y:
                newx = x-y
                newy = y+y
            else:
                newy = y-x
                newx = x+x
            if visited[newx][newy]==False:
                visited[newx][newy]=True
                queue.append([newx,newy,z])
        if x != z:
            if x>z:
                newx = x-z
                newz = z+z
            else:
                newz = z-x
                newx = x+x
            if visited[newx][newz]==False:
                visited[newx][newz]=True
                queue.append([newx,y,newz])
        if y != z:
            if y>z:
                newy = y-z
                newz = z+z
            else:
                newz = z-y
                newy = y+y

            if visited[newy][newz]==False:
                visited[newy][newz]=True
                queue.append([x,newy,newz])
    return 0 #while문을 빠져나와도 reutrn 값이 없으면 같은 수를 만들 수 없으므로 retur 0 

a,b,c = map(int,input().split())
visited = [[False]*1501 for _ in range(1501)]
print(func(a,b,c))            
        

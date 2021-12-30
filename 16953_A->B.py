import sys
input=sys.stdin.readline
from collections import deque

a, b = map(int,input().split())

def bfs(x,cnt):
    queue=deque()
    queue.append((x,cnt))

    while queue:
        x,cnt = queue.popleft()

        if x ==b:#b로 만들었을 경우 연산횟수 리턴하며 중단 
            return cnt
        elif x<b: #아직 b로 만들지 못한 경우 각각의 연산 실행
            nx1 = int(str(x)+"1")
            nx2 = x*2
            cnt+=1
            queue.append((nx1,cnt))
            queue.append((nx2,cnt))

    return -2 #a를 b로 만들 수 없는 경우 마지막에 +1해주므로 -2를 리턴 

print(bfs(a,0)+1)

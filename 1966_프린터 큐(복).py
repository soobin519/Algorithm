import sys
input = sys.stdin.readline
from collections import deque

x = int(input())

for i in range(x):
    n,m = map(int, input().split())
    star = deque(map(int, input().split())) #큐에 문서의 중요도 등록 
    queue = deque(i for i in range(n))

    cnt = 0

    while True:
        smax = max(star)

        if star[0]==smax:
            cnt+=1 #출력 횟수 +1
            if queue[0] == m: #출력해야할 문서라면
                print(cnt)
                break
            star.popleft()
            queue.popleft()
        else: #중요도가 가증 크지 않으면 뒤로 넘김
            star.append(star.popleft())
            queue.append(queue.popleft())

    

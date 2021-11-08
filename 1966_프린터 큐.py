from collections import deque
import sys
input = sys.stdin.readline

a = int(input())

for i in range(a):
    n, m = map(int, input().split())
    star=deque(map(int, input().split()))
    queue = deque(i for i in range(n))

    cnt=0
    while True:
        smax=max(star)

        if star[0]==smax:
            cnt+=1
            if queue[0]==m:
                break
            star.popleft()
            queue.popleft()
        else:
            star.append(star.popleft())
            queue.append(queue.popleft())

    print(cnt)
        

    

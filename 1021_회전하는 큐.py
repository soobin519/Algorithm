import sys
input =sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
pop_list = list(map(int, input().split()))
cnt=0
num = deque([i for i in range(1,N+1)])

for i in pop_list:
    if num.index(i)==0: #1번 연산
        num.popleft()
    elif num.index(i)<=len(num)//2: #2번 연산 
        while num.index(i)!=0:
            cnt+=1
            num.append(num.popleft())
        num.popleft()
    elif num.index(i)>len(num)//2: #3번 연산
        while num.index(i)!=0:
            cnt+=1
            num.appendleft(num.pop())
        num.popleft()
print(cnt)

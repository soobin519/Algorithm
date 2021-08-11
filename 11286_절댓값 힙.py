import sys
input = sys.stdin.readline
N = int(input())

import heapq
heap = []

for i in range(N):
    x = int(input())
    if x!=0: heapq.heappush(heap,(abs(x),x))
    else:
        if len(heap)==0: print(0)
        else: print(heapq.heappop(heap)[1])

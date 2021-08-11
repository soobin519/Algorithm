import sys
input = sys.stdin.readline
N= int(input())

#힙큐 모듈을 통해 원소를 추가,삭제하면 그 자체가 최소 힙 
#최소힙 : 루트 노트가 가장 작은 값을 가짐
import heapq
heap = []

for i in range(N):
    x = int(input())
    if x != 0: #x가 자연수이면 
        heapq.heappush(heap,x)
        print(heap)
    else: #x가 0이면
        if len(heap)==0: #배열이 비어있으면
            print(0)
        else:
            print(heapq.heappop(heap))
        

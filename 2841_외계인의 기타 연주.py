import sys
input = sys.stdin.readline

n, p = map(int,input().split())
g = [[] for _ in range(7)]

cnt=0
for i in range(n):
    line, pnum = map(int,input().split())

    if len(g[line])==0:
        g[line].append(pnum)
        cnt+=1
    else:
        if pnum>g[line][-1]: #새로운 프렛의 번호가 더 클 경우
            g[line].append(pnum)#(손가락 뗄 필요x,바로 누르기)
            cnt+=1
        elif pnum<g[line][-1]:#새로운 프렛의 번호가 더 작을 경우 
            while True: 
                if len(g[line])==0 or pnum>g[line][-1]:
                #스택이 비거나 프렛이 더 크면 손가락 떼기를 멈추 누르기 
                    g[line].append(pnum)
                    cnt+=1
                    break
                elif pnum==g[line][-1]: #프렛의 번호가 같으면 추가 x
                    break             
                else: #새로운 프렛의번호가 계속 작으면 계속 손가락 떼기 
                    g[line].pop()
                    cnt+=1
print(cnt)

import sys
input = sys.stdin.readline
from itertools import combinations as cb

n = int(input())
arr = []
t,b = [],[]
for i in range(n):
    arr.append(list(map(str,input().rstrip().split())))
    for j in range(n):
        if arr[i][j] == "T": #선생님 위치 저장 
            t.append([i,j])
        elif arr[i][j] =="X": #빈칸 위치 저장 
            b.append([i,j])

dx = [-1,0,1,0]
dy = [0,-1,0,1]

#감시 피할 수 있는지 check 
def check():       
    for a in t:#선생님 위치 
        for i in range(4):
            x = a[0]
            y = a[1]
            while True:
                #점점 멀어지면서 검사 
                x+=dx[i]
                y+=dy[i]

                #범위를 벗어나거나 장애물이 있으면 중단
                if x < 0 or x > n - 1 or y < 0 or y > n - 1 or arr[x][y]=="O": 
                    break
                if arr[x][y]=="S": #해당 라인에 학생이 존재하면
                    return 0
    return 1

answer =0
#장애물 설치 
def set():
    for o in cb(b,3): #빈칸 중 조합으로 장애물 선택 
        for i,j in o:
            arr[i][j]='O'

        global answer
        answer+= check() #감시를 피하는지 검사 
        if answer>0: break

        for i,j in o:
            arr[i][j] ='X'

set()

if answer==0:
    print("NO")
else:
    print("YES")

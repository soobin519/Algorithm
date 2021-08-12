import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cnt=0
board =[]
count = []

for n in range(N):
    board.append(input())
    
for n in range(N-7): #세로
    for m in range(M-7): #가로
        cnt1 = 0
        cnt2 = 0
        for i in range(8):
            for j in range(8):
                if (n+i+m+j)%2 == 0:
                    if board[n+i][m+j]!= 'W': cnt1+=1
                    if board[n+i][m+j]!= 'B': cnt2+=1
                else:
                    if board[n+i][m+j]!= 'B': cnt1+=1
                    if board[n+i][m+j]!= 'W': cnt2+=1
        count.append(min(cnt1,cnt2))
print(min(count))

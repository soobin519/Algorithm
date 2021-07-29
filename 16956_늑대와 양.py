import sys

R, C = map(int, sys.stdin.readline().split()) #목장의 크기 읽어와서 int형으로 변환
#strip():문자열 공백 제거  
board = [list(sys.stdin.readline().strip()) for i in range(R)] #목장 입력 불러옴
dx = [-1,1,0,0]
dy = [0,0,-1,1]
flag = 0
         
for r in range(R):
         for c in range(C):
             #늑대일 경우 
             if board[r][c] == 'W':
                 for i in range(4):
                     nr = r+dx[i]
                     nc = c+dy[i]
                     if nr<0 or nr>=R or nc<0 or nc>=C:
                         continue
                     elif board[nr][nc] =='S': #늑대와 양 인접했다면
                         flag=1
                     
             elif board[r][c] == 'S':
                 continue
             else:
                board[r][c] ='D'
if flag == 1:
    print('0')
else:
    print('1')
    for i in board:
        print(''.join(i))
        

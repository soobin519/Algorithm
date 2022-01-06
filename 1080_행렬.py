n, m = map(int,input().split())
a = [list(map(int, input())) for _ in range(n)]
b = [list(map(int, input())) for _ in range(n)]

#3×3크기의 부분 행렬 원소 뒤집기 
def change(x,y):
    for i in range(x,x+3):
        for j in range(y,y+3):
            if a[i][j]==0:
                a[i][j]=1
            else:
                a[i][j]=0

#a행렬에서 b행렬과 다른 부분 찾기 
cnt=0
for i in range(n-2):
    for j in range(m-2):
        if a[i][j]!=b[i][j]:
            change(i,j)
            cnt+=1

if a==b: #a와 b행렬을 같게 만들었으면 cnt 출력
    print(cnt)
else:
    print(-1)

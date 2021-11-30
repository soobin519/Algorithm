import sys
input = sys.stdin.readline

def one(): #연산1
    temp = [ [0 for _ in range(m)] for _ in range(n)]
    for i in range(n):        
        temp[i] = data[n-i-1]
    return temp

def two(): #연산2
    temp = [ [0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            temp[i][j] = data[i][m-j-1]
    return temp

def three(data,n,m): #연산3
    temp = [ [0 for _ in range(n)] for _ in range(m)]
    for j in range(n):
        for i in range(m):
            temp[i][j]= data[n-j-1][i]
    return temp
    

def four(data,n,m): #연산4
    temp = [ [0 for _ in range(n)] for _ in range(m)]
    for j in range(n):
        for i in range(m):
            temp[i][j]= data[j][m-i-1]
    return temp

def five(): #연산5
    temp = [ [0 for _ in range(m)] for _ in range(n)]
    #그룹1->2  
    for i in range(n//2):
        for j in range(m//2):
            temp[i][j+m//2]=data[i][j]
    #그룹2->3
    for i in range(n//2):
        for j in range(m//2,m):
            temp[i+n//2][j]=data[i][j]
    #그룹3->4  
    for i in range(n//2,n):
        for j in range(m//2,m):
            temp[i][j-m//2]=data[i][j]  
    #그룹4->1  
    for i in range(n//2,n):
        for j in range(m//2):
            temp[i-n//2][j]=data[i][j]
    return temp

def six():
    temp = [ [0 for _ in range(m)] for _ in range(n)]
    #그룹1->4  
    for i in range(n//2):
        for j in range(m//2):
            temp[i+n//2][j]=data[i][j]
    #그룹2->1
    for i in range(n//2):
        for j in range(m//2,m):
            temp[i][j-m//2]=data[i][j]
    #그룹3->2  
    for i in range(n//2,n):
        for j in range(m//2,m):
            temp[i-n//2][j]=data[i][j]  
    #그룹4->3 
    for i in range(n//2,n):
        for j in range(m//2):
            temp[i][j+m//2]=data[i][j]
    return temp

#입력 
n,m,r  = map(int, input().split())
data = [ list(map(int,input().split())) for _ in range(n)]
oper = list(map(int, input().split()))

#연산 수행 
for a in range(r):
    if oper[a] ==1:
        data =one()
    elif oper[a] ==2:
        data =two()
    elif oper[a] ==3:
        data =three(data,n,m)
        n, m = m, n
    elif oper[a] ==4:
        data =four(data,n,m)
        n, m = m, n
    elif oper[a] ==5:
        data =five()
    else:
        data=six()

#결과 출력 
for i in data:
    print(*i)



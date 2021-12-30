import sys
input = sys.stdin.readline

a,b,c= map(int,input().split())

def cal(a,b,c):
    if b==1:
        return a%c
    
    if b%2==0: #짝수이면
        return (cal(a,b//2,c)**2)%c
    else:#홀수이면
        return (cal(a,b//2,c)**2*a)%c
print(cal(a,b,c))

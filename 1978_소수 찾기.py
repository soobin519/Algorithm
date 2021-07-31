import sys

n= int(sys.stdin.readline())
num = list(sys.stdin.readline().split())
answer=0
for i in num:
    if int(i)==1: continue
    for j in range(2,int(i)):
        if int(i)%j == 0:
            break
    else:
        answer+=1
print(answer)
    
    

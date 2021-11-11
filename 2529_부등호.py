#백트래킹 
import sys
input = sys.stdin.readline

k=int(input())
sign = list(map(str, input().split()))

visited=[False]*10
max_ans =""
min_ans =""


def check(i,j,k): #부등호 체크 
    if k=='<':
        return i<j
    else:
        return i>j

def func(idx,s):
    global max_ans,min_ans
    
    if idx==k+1: #탈출조건
        if(len(min_ans)==0):
            min_ans = s
        else:
            max_ans = s
        return
    
    for i in range(10):
        if not visited[i]: #방문하지 않았으면 
            if idx==0 or check(s[-1],str(i),sign[idx-1]): #처음이거나 부등호 성립하면
                visited[i]=True
                func(idx+1,s+str(i))
                visited[i]=False
    

func(0,"")
print(max_ans)
print(min_ans)


        

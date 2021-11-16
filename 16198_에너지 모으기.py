import sys
input = sys.stdin.readline

n = int(input())
w = list(map(int, input().split()))
max_r= 0
         
def func(result):
    global max_r
    #print("W",w)
    if len(w)==2: #중단 조건
        max_r = max(max_r, result)
        return

    for i in range(1,len(w)-1): #처음과 마지막은 선택x
        #print("choice", w[i])
        sum_r= (w[i-1]*w[i+1])
        result += sum_r
        #print("sum_r", sum_r) 
        #print("result",result)         
        temp=w[i] #삭제전 임시로 저장해두기 
        del w[i]          
        func(result)
        w.insert(i,temp)
        result-=sum_r
        #print("when",result)       
        
func(0)
print(max_r)

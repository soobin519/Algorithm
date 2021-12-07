import sys
input = sys.stdin.readline

i=1 #테스트 케이스 index
while True:    
    s=input()
    stack = []
    cnt=0
    
    if "-" in s: break #테스트케이스 중단 조건 

    for a in s:
        if a=="{":
            stack.append(a)
        elif a=="}":
            if "{" not in stack:
                cnt+=1
                stack.append("{") #바궈줌 
            else:
                stack.pop()

    #stack 에는 "{" 만 담겨있음 
    cnt+= len(stack)//2
    print(f'{i}. {cnt}')
    i+=1 #다음 테스트케이스로 

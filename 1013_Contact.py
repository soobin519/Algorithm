import sys
input = sys.stdin.readline

#(100+1+ | 01)+
for i in range(int(input())):
    s = input().rstrip()
    result =True

    while len(s)>0:
        if s.startswith("100"):
            s = s[3:] #"100"제거 

            while len(s)>0 and s.startswith("0"): #0+에 0이 계속 나오는 경우 
                s=s[1:] #맨 처음 "0" 제거 

            if len(s)==0: #뒤에 1이 무조건 하나는 나와야하므로 False
                result=False
                break
            
            s=s[1:] #맨 처음 "1"이나오는 경우 1제거
            #여기까지 진행하면 100+1 은 만족           

            while len(s)>0 and s.startswith("1"): 
                if len(s)>=3 and s[1]=="0" and s[2]=="0": #"100"이 나오는 경우 고려를 위해 보류
                    break
                else: #1+에 1이 계속 나오는 경우
                    s=s[1:]
    
        elif s. startswith("01"):
            s = s[2:] #"01"제거 

        else:
            result=False
            break

    #결과 출력 
    if result: print("YES")
    else: print("NO")

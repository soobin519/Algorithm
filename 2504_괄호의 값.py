data = input()

tmp=1
answer=0
stack=[]

for i in range(len(data)):
    #print (stack)
    #print("Tmp",tmp)
    #print("answer",answer)

    if data[i] == "(":
        stack.append(data[i])
        tmp *= 2

    elif data[i] == "[":
        stack.append(data[i])
        tmp *= 3

    elif data[i] == ")":
        if not stack or stack[-1] == "[": #괄호의 쌍이 성립하지 않으면 
            answer = 0
            break 
        if data[i-1] == "(":
            answer += tmp
        stack.pop()
        tmp //= 2

    else: #if data[i]=="]" 
        if not stack or stack[-1] == "(": #괄호의 쌍이 성립하지 않으면 
            answer = 0
            break
        if data[i-1] == "[":
            answer += tmp
        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(answer)


N, M = int(input()), int(input())
S = input()

i, cnt, result = 1, 0, 0
while i<M-1:
    if S[i-1:i+2]=='IOI':
        cnt+=1
        if cnt==N:
            result+=1
            cnt-=1
        i+=1
    else:
        cnt =0
    i+=1
print(result)

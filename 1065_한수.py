n = int(input())
cnt=0

for i in range(1, n+1):
    if i>=1 and i<=99: cnt+=1
    else:
        s=str(i)
        for j in range(1,len(s)-1):
            if int(s[j])-int(s[j+1])!=int(s[0])-int(s[1]): break
        else:
            cnt+=1
print(cnt)
     

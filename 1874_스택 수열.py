import sys
input=sys.stdin.readline

n = int(input())
temp = []
result = []
cnt=1

for i in range(n):
    a = int(input())
    while cnt<=a:
        temp.append(cnt)
        result.append('+')
        cnt+=1

    if temp[-1]==a:
        temp.pop()
        result.append('-')
    else:
        print("NO")
        exit(0)
        
for i in result: print(i)

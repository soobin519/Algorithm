import sys
input = sys.stdin.readline

a =input().rstrip().split('-')
answer = []

for i in range(len(a)):
    b= a[i].split('+')
    n=0
    for i in b:
        n+=int(i)
    answer.append(n)

result=answer[0]
for i in range(1,len(answer)): result-=answer[i]
print(result)
        

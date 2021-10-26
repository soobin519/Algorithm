import sys
input = sys.stdin.readline

N=int(input())
lope=[]

for i in range(N):
    lope.append(int(input()))
lope.sort(reverse=True)

result=[]
for k in range(N):
    result.append(lope[k]*(k+1))
    
print(max(result))

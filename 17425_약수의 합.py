import sys
input = sys.stdin.readline

#n의 최대값: 1000000
f = [1]*1000001 #약수의 합 저장(모든 수는 1은 약수로 가지므로 1로 초기화 )
g = [0]*1000001 #f의 합 

#약수의 합 저장 - f(1)=1
#최대값까지 저장해두고 시작하기 위함 
for i in range(2,1000001):
    j =1
    while i*j<=1000000:
        f[i*j]+=i
        j+=1

#g(i) = g(i-1)+f(i)        
for i in range(1,1000001):
    g[i] = g[i-1]+f[i]

ans = []   
for i in range(int(input())):
    n = int(input())   
    ans.append(g[n])
    
print('\n'.join(map(str, ans))+'\n')

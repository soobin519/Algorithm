import sys
input = sys.stdin.readline

n=int(input())
s=[0]

#두번째 계단일 경우
#새로 밟는 경우 

for i in range(n):
    s.append(int(input()))

g = [0,0]
h = [0,s[1]]

for i in range(2,n+1):
    g.append(h[i-1]+s[i])
    h.append(max(h[i-2],g[i-2])+s[i])
  
print(max(g[n],h[n]))

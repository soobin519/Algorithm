k=int(input())
a=[0 for i in range(k+1)]

for i in range(k+1):
    if i==0: continue
    elif i==1: a[i]=1
    else:
        a[i]=a[i-1]+a[i-2]
        
print(a[-2], a[-1])

#피보나치 수열 원리를 이용할것..

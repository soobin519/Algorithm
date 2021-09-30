import sys
input=sys.stdin.readline
E,S,M=map(int,input().split())

i=1
while True:
    #if i%15==E and i%28==S and i%19==M:
    if (i-E)%15==0 and (i-S)%28==0 and (i-M)%19==0:
        print(i)
        break
    i+=1

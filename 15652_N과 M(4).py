import sys
input = sys.stdin.readline

n,m = map(int, input().split())
s=[]

def func(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return

    for i in range(start,n+1):
        s.append(i)
        func(i)
        s.pop()
func(1)
        

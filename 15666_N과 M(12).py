import sys
input = sys.stdin.readline

n,m = map(int, input().split())
num = set(map(int, input().split()))
num = sorted(num)
s=[]

def func():
    if len(s)==m:
        print(' '.join(map(str, s)))
        return
    for i in num:
        if len(s)==0 or i>=s[-1]:
            s.append(i)
            func()
            s.pop()
func()

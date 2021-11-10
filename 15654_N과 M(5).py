import sys
input = sys.stdin.readline

n,m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
s=[]

def func():
    if len(s)==m:
        print(' '.join(map(str, s)))
        return
    for i in num:
        if i not in s:
            s.append(i)
            func()
            s.pop()
func()

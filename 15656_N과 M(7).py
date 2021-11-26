import sys
input = sys.stdin.readline

n,m = map(int,input().split())
nlist = list(map(int,input().split()))
nlist.sort() #오름차순 배열
result=[] #결과를 담을 list

def func():
    if len(result)==m: #모두 선택하면 print
        print(' '.join(map(str,result)))
        return
    for i in range(n):
        result.append(nlist[i])
        func()
        result.pop()

func()

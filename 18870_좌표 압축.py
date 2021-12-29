import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int,input().split()))
x2 = sorted(set(x))

#딕셔너리로 만들기
dic = {x2[i]:i for i in range(len(x2))}

for i in range(n):
    print(dic[x[i]], end=' ')

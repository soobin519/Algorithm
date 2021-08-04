T = int(input())

for i in range(T):
    data = input()

    cnt1, cnt2 = 0, 0
    for j in data:
        if j =="(": cnt1+=1
        elif j==")": cnt2+=1
        #오른쪽 괄호가 더 많은 경우
        if cnt1<cnt2:
            print("NO")
            break
    else:
        #오른쪽괄호와 왼쪽괄호의 개수가 다른 경우 
        if cnt1 != cnt2:
            print("NO")
        else:
            print("YES")


#스택의 개념을 이용하면 더 간단한 풀이가 가능하다.
#solution2
from sys import stdin

n = int(input())
for _ in range(n):
    str_ = stdin.readline().strip()
    stack = 0
    for chr_ in str_:
        if chr_ == '(':
            stack += 1
        else:
            stack -= 1
            if stack < 0:
                break
    if stack == 0:
        print('YES')
    else:
        print('NO')

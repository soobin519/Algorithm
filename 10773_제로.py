import sys
input = sys.stdin.readline

K = int(input())
result = []
for i in range(K):
    num = int(input())
    if num !=0: #숫자 추가
        result.append(num)
    else: #숫자를 지워야하면
        result.pop()
print(sum(result))

#브루트포스 알고리즘: 무식하기 풀기(완전 탐색 알고리즘) 
n = int(input())
num = 666
result = 0

while result <n-1:
    num+=1
    if '666' in str(num):
        result+=1
    
print(num)

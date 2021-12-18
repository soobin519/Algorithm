import sys
input = sys.stdin.readline

for i in range(int(input())):
    n = int(input()) #지원자 숫자
    rank = [ list(map(int,input().split())) for _ in range(n)]
    rank.sort()

    result = []
    j=0
    for i in range(1,n):
        if rank[i][1]<rank[j][1]:
            result.append(rank[i])
            j =i

    print(len(result)+1)


    

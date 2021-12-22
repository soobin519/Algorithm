import sys
input = sys.stdin.readline

for i in range(int(input())):
    n = int(input()) #지원자 숫자
    rank = [ list(map(int,input().split())) for _ in range(n)] #서류심사 성적, 면접 성적
    rank.sort() #서류심사 성적 기준으로 정렬 

    result = []
    j=0 #서류 성적이 높은 지원자의 index
    for i in range(1,n): #면접 성적 비교 
        if rank[i][1]<rank[j][1]: #서류 성적이 낮은 지원자 중 면접 성적이 높으면 
            result.append(rank[i])
            j =i

    print(len(result)+1) #맨 처음 사람 포함하기 위해 +1


    

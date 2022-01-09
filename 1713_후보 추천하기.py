import sys
input = sys.stdin.readline
#반례
#3
#10
#3 4 3 3 1 2 4 1 5 7

n = int(input())
k = int(input())
lis = list(map(int,input().split()))
candi = [0]*n #후보 자리 
cnt = [0]*n #후보 추천수 저장 

for i in range(k):
    if lis[i] in candi: #이미 등록된 후보라면 
        cnt[candi.index(lis[i])]+=1
    else:
        if 0 in candi: #비어있는 자리가 존재하면 
            candi.remove(0)
            candi.append(lis[i])
            cnt.remove(0)
            cnt.append(1)            
        else: #비어있는 자리가 없는 경우, 추천 받은 횟수가 가장 적은 후보 삭제
            a = cnt.index(min(cnt)) #추천 횟수가 가장 적은 후보 인덱스 찾기 
            candi.remove(candi[a])
            candi.append(lis[i])
            cnt.remove(cnt[a])
            cnt.append(1) 

candi = list(set(candi)) #중복 제거를위해 집합 사용 
if 0 in candi:
    candi.remove(0)
candi.sort()
print(*candi)

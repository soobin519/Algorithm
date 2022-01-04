import sys
input = sys.stdin.readline

n, m =map(int,input().split()) #사람 수, 파티 수 
know=set(input().split()[1:])
pnum=[]
cnt = 0

#파티 참가 정보 등록 
for i in range(m):
    pnum.append(set(input().split()[1:]))
print(pnum)

#진실을 아는 사람 정보 등록 
for i in range(m):
    for party in pnum:
        if party &know: #진실을 아는 사람이 겹치면 know에 추가 (교집합)
            know.update(party) #집합에 여러개를 추가할때는 update함수 사용!      
print("최종 know",know)

for i in range(m):
    for t in pnum[i]:
        if t in know: #진실을 아는 사람이 있을 경우 cnt+=1
            cnt+=1
            break
print(m-cnt) #전체에서 진실만을 말해야하는 경우를 뺀다.

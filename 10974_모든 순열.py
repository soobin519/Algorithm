from itertools import permutations as per

N = int(input())
num_list=[]

for i in range(1,N+1):
    num_list.append(str(i))
result=list(map(' '.join, per(num_list,N)))
for i in result:
    print(i)


    

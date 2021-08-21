import sys
input = sys.stdin.readline

zero = [1,0]
one = [0,1]
for i in range(2,41):
    zero.append(one[i-1])
    one.append(zero[i-1]+one[i-1])   
    
T = int(input())
for i in range(T):
    n = int(input())
    print(zero[n], one[n])



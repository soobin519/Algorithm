n = int(input())
lis = [input() for _ in range(n)]
k=1
print({i[-k:] for i in lis})
while True:
    if len({i[-k:] for i in lis})==n:
        print(k)
        break
    k+=1

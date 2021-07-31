temp =set(range(1,10001))
made = set()
for i in range(1,10001):
    answer = i
    for j in str(i):
        answer+=int(j)
    made.add(answer)
self_number = sorted(temp-made)
for i in self_number:
    print(i)
    

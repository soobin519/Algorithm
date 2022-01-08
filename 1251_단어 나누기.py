s = input()
li = []
for i in range(len(s)-2):
    for j in range(i+1, len(s)-1):
        for k in range(j+1, len(s)):
            #[::-1]처음부터 끝까지 -1칸 간격으로(역순으로)
            t = s[:j][::-1] + s[j:k][::-1] + s[k:][::-1]
            li.append(t)
print(min(li))

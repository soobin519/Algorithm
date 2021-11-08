import sys
input = sys.stdin.readline

s = input()
change=[s[0]]

for i in range(1,len(s)):
    if s[i]!=change[-1]:
        change.append(s[i])
cnt0 = change.count("0")
cnt1 = change.count("1")
print(min(cnt0,cnt1))


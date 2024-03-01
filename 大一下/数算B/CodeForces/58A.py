s = input()
t = 'hello'

i = 0
tag = False
for j in range(len(s)):
    if s[j]==t[i]:
        i += 1
    if i==5:
        tag = True
        break
if tag:
    print('YES')
else:
    print('NO')

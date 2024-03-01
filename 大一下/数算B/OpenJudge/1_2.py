s = input().split('+')

def com(x):
    if x[0]=='0':
        return 0
    else:
        a, b = x.split('^')
        return int(b)

s_com = [com(item) for item in s]
ans = max(s_com)
print('n^%d' % ans)

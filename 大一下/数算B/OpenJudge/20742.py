def t(x):
    if x==0:
        return 0
    elif x==1 or x==2:
        return 1
    else:
        return t(x-1) + t(x-2) + t(x-3)


n = int(input())
k = t(n)
print(k)

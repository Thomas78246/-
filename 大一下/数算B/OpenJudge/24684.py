select = dict()
votes = [int(i) for i in input().split()]
for i in votes:
    if i in select:
        select[i] += 1
    else:
        select[i] = 1
M = max(select.values())
champion = [key for (key, value) in select.items() if value==M]
champion.sort()
print(*champion)

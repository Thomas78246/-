n, w = map(int, input().split())
candy = [list(map(int, input().split())) for _ in range(n)]
candy.sort(key=lambda o:o[0]/o[1], reverse=True)
value = 0
for i in range(n):
    if w >= candy[i][1]:
        value += candy[i][0]
        w -= candy[i][1]
    elif 0 < w < candy[i][1]:
        value += w * candy[i][0] / candy[i][1]
        # w = 0
        break
    else:
        break
print('%.1f' % value)

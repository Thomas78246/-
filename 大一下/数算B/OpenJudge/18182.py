nCases = int(input())
for _ in range(nCases):
    n, m, b = map(int, input().split())
    move = [list(map(int, input().split())) for _ in range(n)]
    move.sort(key=lambda x:(x[0], -x[1]))
    tm, t_current, move_left = -1, -1, m
    for ti, xi in move:
        if ti!=t_current:
            t_current = ti
            move_left = m-1
            b -= xi
        elif move_left > 0:
            move_left -= 1
            b -= xi
        else:
            pass
        if b <= 0:
            tm = ti
            break
    if tm>=0:
        print(tm)
    else:
        print('alive')

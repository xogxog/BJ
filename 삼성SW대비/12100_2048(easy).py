from copy import deepcopy
n = int(input())
games = [list(map(int, input().split())) for _ in range(n)]
move_d = ('up', 'down', 'right', 'left')
ans = 0


def turn(ls):  # 왼쪽으로 옮기는 방법
    tmp = [[0]*n for _ in range(n)]
    chk = [[0]*n for _ in range(n)]  # 합쳐진 곳
    for i in range(n):
        for j in range(n):
            if j == 0:
                tmp[i][j] = ls[i][j]
            elif ls[i][j]:  # 옮길 블록 있음
                now = ls[i][j]
                for k in range(j-1, -1, -1):
                    if tmp[i][k] == 0:  # 옮김 가능
                        if k == 0:  # 마지막까지 왔으면
                            tmp[i][k] = now
                        else:
                            continue
                    elif tmp[i][k] == now and not chk[i][k]:
                        chk[i][k] = 1
                        tmp[i][k] = now*2
                        break
                    else:
                        tmp[i][k+1] = now
                        break
    return tmp


def rotate(ls, direc):
    tmp = [[0]*n for _ in range(n)]
    if direc == 'l':
        for i in range(n):
            for j in range(n):
                tmp[n-j-1][i] = ls[i][j]
    elif direc == 'r':
        for i in range(n):
            for j in range(n):
                tmp[j][n-i-1] = ls[i][j]
    else:
        for i in range(n):
            tmp[i] = ls[i][::-1]
    return tmp


def start(game, cnt):
    global ans

    if cnt >= 5:  # 여기서 틀림,, cnt > 5라고했슴,,
        tmp_ans = 0
        for i in range(n):
            tmp_ans = max(tmp_ans, max(game[i]))
        ans = max(ans, tmp_ans)
        return

    for move in move_d:
        if move == 'up':
            tmp_ls = rotate(turn(rotate(game, 'l')),
                            'r')  # 왼 90도, 되돌리기
            start(tmp_ls, cnt+1)
        elif move == 'down':
            tmp_ls = rotate(turn(rotate(game, 'r')), 'l')
            start(tmp_ls, cnt+1)
        elif move == 'right':
            tmp_ls = rotate(turn(rotate(game, 'oppo')), 'oppo')
            start(tmp_ls, cnt+1)
        elif move == 'left':
            tmp_ls = turn(game)
            start(tmp_ls, cnt+1)


start(games, 0)
print(ans)

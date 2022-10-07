from copy import deepcopy


n, m = map(int, input().split())

arr = [list(input().rstrip()) for _ in range(n)]
visited = set()
ans = 11


def rotate(arr, d):
    _n, _m = len(arr), len(arr[0])
    if d == 'l':
        tmp = [[0]*_n for _ in range(_m)]
        for i in range(_n):
            for j in range(_m):
                tmp[_m-j-1][i] = arr[i][j]
    elif d == 'r':
        tmp = [[0]*_n for _ in range(_m)]
        for i in range(_n):
            for j in range(_m):
                tmp[j][_n-i-1] = arr[i][j]
    else:  # 위아래 데칼코마니
        tmp = [[0]*_m for _ in range(_n)]
        for i in range(_n):
            tmp[_n-i-1] = arr[i][:]
    return tmp


def move(arr):  # 아래로 떨어지게 구현
    _n, _m = len(arr), len(arr[0])
    for i in range(_n-2, 0, -1):
        for j in range(1, _m-1):
            if arr[i][j] in ('B', 'R'):
                r = i
                for k in range(i+1, _n):
                    # 벽에 부딪히거나 구슬에 부딪힌 경우
                    if arr[k][j] == '#' or arr[k][j] in ('B', 'R'):
                        arr[k-1][j] = arr[i][j]
                        if (k-1, j) != (i, j):  # 원래 구슬 있던 자리 . 으로 처리
                            arr[i][j] = '.'
                        break
                    # 구멍에 빠진 경우
                    if arr[k][j] == 'O':
                        arr[i][j] = '.'
                        break

    return arr


def is_visited(arr, cnt):  # 방문체크 or 도착여부 판단
    global end
    now_b = (0, 0)
    now_r = (0, 0)

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'R':
                now_r = (i, j)
            if arr[i][j] == 'B':
                now_b = (i, j)
    if now_r == (0, 0) and now_b == (0, 0):  # 둘 다 도착
        return True, False
    elif now_r == (0, 0) and now_b != (0, 0):  # 빨간색만 도착
        return True, True
    elif now_r != (0, 0) and now_b == (0, 0):  # 파란색만 도착
        return True, False
    else:                              # 둘다 도착 X
        if (now_b, now_r, cnt) in visited:  # 방문한 적 있음
            return False, True
        else:                          # 방문한 적 없음
            visited.add((now_b, now_r, cnt))
            return False, False


def bfs(arr, cnt):
    global ans
    if cnt > 10:
        return
    # 왼
    moved_ls = rotate(move(rotate(deepcopy(arr), 'l')), 'r')
    flag, r_goal = is_visited(moved_ls, cnt)

    if flag and r_goal:
        ans = min(ans, cnt)
        return
    elif flag and not r_goal:
        return
    elif not flag and not r_goal:
        bfs(moved_ls, cnt+1)

    # 오
    moved_ls = rotate(move(rotate(deepcopy(arr), 'r')), 'l')
    flag, r_goal = is_visited(moved_ls, cnt)

    if flag and r_goal:
        ans = min(ans, cnt)
        return
    elif flag and not r_goal:
        return
    elif not flag and not r_goal:
        bfs(moved_ls, cnt+1)

    # 아래
    moved_ls = move(deepcopy(arr))
    flag, r_goal = is_visited(moved_ls, cnt)

    if flag and r_goal:
        ans = min(ans, cnt)
        return
    elif flag and not r_goal:
        return
    elif not flag and not r_goal:
        bfs(moved_ls, cnt+1)

    # 위
    moved_ls = rotate(move(rotate(deepcopy(arr), 'oppo')), 'oppo')
    flag, r_goal = is_visited(moved_ls, cnt)

    if flag and r_goal:
        ans = min(ans, cnt)
        return
    elif flag and not r_goal:
        return
    elif not flag and not r_goal:
        bfs(moved_ls, cnt+1)


end = (0, 0)
r_ball = (0, 0)
b_ball = (0, 0)
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'O':
            end = (i, j)
        if arr[i][j] == 'R':
            r_ball = (i, j)
        if arr[i][j] == 'B':
            b_ball = (i, j)
visited.add((b_ball, r_ball, 0))  # 출발지점 체크,,위해서인데 딱히 필요없을 듯

bfs(arr, 1)
print(ans if ans < 11 else -1)

import sys
from collections import deque

input = sys.stdin.readline
drc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
puyo = [list(input().rstrip()) for _ in range(12)]
ans = 0


def bfs(alpha, x, y):
    q = deque()
    q.append((x, y))
    ls = [(x, y)]
    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + drc[i][0]
            nc = c + drc[i][1]
            if 0 <= nr < 12 and 0 <= nc < 6 and not visited[nr][nc] and puyo[nr][nc] == alpha:
                visited[nr][nc] = 1
                q.append((nr, nc))
                ls.append((nr, nc))
    return ls


def destroy(ls):
    for r, c in ls:
        puyo[r][c] = '.'


while 1:
    visited = [[0] * 6 for _ in range(12)]
    d_cnt = 0  # 뿌셨는지 체크
    for i in range(12):
        for j in range(6):
            if puyo[i][j] != '.' and not visited[i][j]:
                visited[i][j] = 1
                destroy_ls = bfs(puyo[i][j], i, j)
                if len(destroy_ls) >= 4:
                    d_cnt += 1
                    destroy(destroy_ls)

    if d_cnt:
        ans += 1
    else:
        break  # 뿌실거 없으니까 break

    # 내리기
    for i in range(10, -1, -1):  # 맨 밑줄은 체크할 필요 없음
        for j in range(5, -1, -1):
            if puyo[i][j] != '.' and puyo[i + 1][j] == '.':
                idx = i + 1
                while idx + 1 < 12 and puyo[idx + 1][j] == '.':
                    idx += 1
                puyo[idx][j], puyo[i][j] = puyo[i][j], '.'

    if puyo[11][:].count('.') == 6:
        break

print(ans)

n = int(input())
ban = [[0]*n for _ in range(n)]
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
# drc = [(0,1),(0,-1),(1,0),(-1,0)]
arr = [list(map(int, input().split())) for _ in range(n**2)]
arr_dict = {}
for i in range(n**2):
    arr_dict[arr[i][0]] = set(arr[i][1:])

for i in range(n**2):
    s = arr[i][0]
    like = set(arr[i][1:])

    if i == 0:  # 첫번째 학생
        ban[1][1] = s
    else:
        like_cnt = -1
        empty = -1
        jari = [0, 0]

        for j in range(n):
            for k in range(n):
                if ban[j][k] != 0:  # 빈자리 아니면
                    continue
                tmp_like_cnt = 0
                tmp_empty = 0
                # for dr, dc in drc:
                #     nr = j+dr
                #     nc = k+dc
                for l in range(4):
                    nr = j+dr[l]
                    nc = k+dc[l]
                    if nr < 0 or nr >= n or nc < 0 or nc >= n:
                        continue
                    if ban[nr][nc] == 0:
                        tmp_empty += 1
                    elif ban[nr][nc] in like:  # 좋아하는 친구 있으면
                        tmp_like_cnt += 1
                if like_cnt < tmp_like_cnt:  # 좋아하는 친구 가장 많은 곳
                    like_cnt = tmp_like_cnt
                    empty = tmp_empty
                    jari = [j, k]
                elif like_cnt == tmp_like_cnt:  # 그런 곳이 많으면
                    if tmp_empty > empty:
                        like_cnt = tmp_like_cnt
                        empty = tmp_empty
                        jari = [j, k]
        ban[jari[0]][jari[1]] = s

ans = 0

for i in range(n):
    for j in range(n):
        get_like = arr_dict[ban[i][j]]
        manjok = 0
        for k in range(4):
            nr = i+dr[k]
            nc = j+dc[k]

            if nr < 0 or nr >= n or nc < 0 or nc >= n:
                continue
            if ban[nr][nc] in get_like:
                manjok += 1
        if manjok:
            ans += 10**(manjok-1)

print(ans)

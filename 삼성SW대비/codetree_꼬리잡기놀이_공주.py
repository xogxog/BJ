def cal_group_routes():
    # 그룹별 이동경로
    groups = []
    visited = [[False] * N for _ in range(N)]
    move_direction = 1
    for _r in range(N):
        for _c in range(N):
            r, c = _r, _c
            # 3 -> 2 -> 1 -> 4 순으로 담기, 3명이상이 한팀
            if arr[r][c] == 3:
                head_tail_idx = (0, 2)
                route = [(r, c)]
                visited[r][c] = True
                for dr, dc in drc:
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < N and 0 <= nc < N) and 0 < arr[nr][nc] == 2:
                        route.append((nr, nc))
                        r, c = nr, nc
                        break

                idx = 1
                while True:
                    visited[r][c] = True

                    for dr, dc in drc:
                        nr, nc = r + dr, c + dc
                        if not (0 <= nr < N and 0 <= nc < N) or visited[nr][nc]:
                            continue

                        if arr[nr][nc]:
                            route.append((nr, nc))
                            r, c = nr, nc
                            idx += 1
                            if arr[r][c] == 1:
                                head_tail_idx = (idx, 0)
                            break

                    else:
                        break
                groups.append([route, head_tail_idx, move_direction])

    return groups


def move(r, c, val):
    arr[r][c] = val


def group_move():
    for i in range(len(groups)):

        route, head_tail_idx, move_direction = groups[i]
        head, tail = head_tail_idx
        next_head = (head + move_direction) % len(route)
        next_tail = (tail + move_direction) % len(route)
        prev_tail = (tail - move_direction) % len(route)

        pr, pc = route[prev_tail]
        prev_val = arr[pr][pc]

        move(*route[next_head], 1)
        move(*route[head], 2)
        move(*route[next_tail], 3)
        move(*route[tail], prev_val)

        groups[i][1] = (next_head, next_tail)


def ball_shoot(r, c, d):
    dr, dc = drc[d]
    for i in range(N):
        nr, nc = r + dr * i, c + dc * i
        if 0 < arr[nr][nc] < 4:
            group_num = group_nums[nr][nc] - 1
            route, head_tail_idx, move_direction = groups[group_num]
            head, tail = head_tail_idx

            groups[group_num][1] = (tail, head)
            groups[group_num][2] = -1 * move_direction

            cnt = 1
            idx = head
            for _ in range(len(route)):
                if route[idx] == (nr, nc):
                    return cnt**2

                cnt += 1
                idx = (idx - move_direction) % len(route)

    return 0


N, M, K = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
drc = [(0, 1), (-1, 0), (0, -1), (1, 0)]

groups = cal_group_routes()
# 해당 위치가 몇번 그룹인지 표시
group_nums = [[0] * N for _ in range(N)]
for i in range(len(groups)):
    route = groups[i][0]
    for r, c in route:
        group_nums[r][c] = i + 1

ball_positions = [  # r, c, d
    *zip(range(N), [0] * N, [0] * N),
    *zip([N - 1] * N, range(N), [1] * N),
    *zip(range(N - 1, -1, -1), [N - 1] * N, [2] * N),
    *zip([0] * N, range(N - 1, -1, -1), [3] * N),
]

score = 0
clearConsole = lambda: os.system("cls" if os.name in ("nt", "dos") else "clear")

for game in range(K):
    group_move()
    # temp = "-------------------------------\n"
    # for r in range(N):
    #     for c in range(N):
    #         if arr[r][c] == 4:
    #             temp += "\033[96m" + f"{arr[r][c]}" + "\033[0m" + " "
    #         elif arr[r][c]:
    #             temp += "\033[95m" + f"{arr[r][c]}" + "\033[0m" + " "
    #         else:
    #             temp += f"{arr[r][c]}" + " "
    #
    #     temp += "\n"
    # clearConsole()
    # print(temp)

    r, c, d = ball_positions[game % (4 * N)]
    score += ball_shoot(r, c, d)
    print(score)

print(score)

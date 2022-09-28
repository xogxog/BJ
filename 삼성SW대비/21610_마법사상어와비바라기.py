import sys
input = sys.stdin.readline

dirc = [(), (0, -1), (-1, -1), (-1, 0), (-1, 1),
        (0, 1), (1, 1), (1, 0), (1, -1)]

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
# cloud = [(N-2, 0), (N-2, 1), (N-1, 0), (N-1, 1)]
cloud = [[0]*N for _ in range(N)]
cloud[N-1][0], cloud[N-1][1], cloud[N-2][0], cloud[N-2][1] = 1, 1, 1, 1

for _ in range(M):
    di, si = map(int, input().split())  # 방향, 길이
    tmp_cloud = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if cloud[i][j] == 1:
                nr = i + dirc[di][0] * si
                nc = j + dirc[di][1] * si

                if nr >= N or nr < 0:
                    nr %= 5
                if nc >= N or nc < 0:
                    nc %= 5
                cloud[i][j] = 0  # 원래 구름 있던 곳은 초기화
                tmp_cloud[nr][nc] = 1  # 1

                A[nr][nc] += 1  # 2

    for i in range(N):
        for j in range(N):
            if tmp_cloud[i][j]:
                ls = [(i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)]
                cnt = 0
                for nr, nc in ls:
                    if 0 <= nr < N and 0 <= nc < N and A[nr][nc]:
                        cnt += 1
                A[i][j] += cnt

    for i in range(N):
        for j in range(N):
            if A[i][j] >= 2 and tmp_cloud[i][j] == 0:
                cloud[i][j] = 1
                A[i][j] -= 2
    # print(f'============cloud')
    # for z in range(N):
    #     print(*cloud[z])
ans = 0
for i in range(N):
    ans += sum(A[i])
print(ans)

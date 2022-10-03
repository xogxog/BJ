import sys
input = sys.stdin.readline

drc = [
    [(0, 1), (1, 1)],
    [(1, 0), (1, 1)],
    [(0, 1), (1, 0), (1, 1)]
]

n = int(input())
home = [list(map(int, input().split())) for _ in range(n)]

dp = [[[0, 0, 0] for _ in range(n)] for __ in range(n)]  # 가로,세로,대각선
dp[0][1] = [1, 0, 0]

for i in range(n):
    for j in range(n):
        for k in range(3):
            if dp[i][j][k]:
                for m_r, m_c in drc[k]:
                    nr = i + m_r
                    nc = j + m_c
                    if 0 <= nr < n and 0 <= nc < n:
                        if m_r == 1 and m_c == 1:  # 대각선인 경우
                            if home[nr][nc] + home[nr-1][nc] + home[nr][nc-1] == 0:
                                dp[nr][nc][2] += dp[i][j][k]
                        else:
                            if not home[nr][nc]:
                                if m_r == 0 and m_c == 1:  # 가로
                                    dp[nr][nc][0] += dp[i][j][k]
                                else:
                                    dp[nr][nc][1] += dp[i][j][k]

print(sum(dp[-1][-1]))

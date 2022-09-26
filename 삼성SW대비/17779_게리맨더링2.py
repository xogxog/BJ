# r,c가 거꾸로 나와서 어렵다,,
import sys

input = sys.stdin.readline


def guyuk(r, c):
    global max_ans
    for d1 in range(1, N):
        for d2 in range(1, N):
            if c + d1 + d2 < N and r - d1 >= 0 and r + d2 < N:  # 5구역을 만들 수 있는 범위
                tmp = [[0] * N for _ in range(N)]
                tmp[r][c] = 5
                # 5구역
                for i in range(1, d1 + 1):
                    tmp[r - i][c + i] = 5
                for i in range(1, d2 + 1):
                    tmp[r + i][c + i] = 5
                for i in range(1, d2 + 1):
                    tmp[r - d1 + i][c + d1 + i] = 5
                for i in range(1, d1 + 1):
                    tmp[r + d2 - i][c + d2 + i] = 5

                one, two, three, four = 0, 0, 0, 0

                # 1구역
                for i in range(r):
                    for j in range(c + d1 + 1):
                        if tmp[i][j] == 5:
                            break
                        one += A[i][j]
                # 3구역
                for i in range(r, N):
                    for j in range(c + d2):
                        if tmp[i][j] == 5:
                            break
                        three += A[i][j]

                # 2구역
                for i in range(r - d1 + d2 + 1):
                    for j in range(N - 1, c + d1, -1):
                        if tmp[i][j] == 5:
                            break
                        two += A[i][j]

                # 4구역
                for i in range(r - d1 + d2 + 1, N):
                    for j in range(N - 1, c + d2 - 1, -1):
                        if tmp[i][j] == 5:
                            break
                        four += A[i][j]

                five = total - (one + two + three + four)
                max_ppl = max(one, two, three, four, five)
                min_ppl = min(one, two, three, four, five)

                max_ans = min(max_ans, max_ppl - min_ppl)


N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
total = 0
max_ans = 400001
for i in range(N):
    total += sum(A[i])

for i in range(1, N - 1):
    for j in range(N - 2):
        guyuk(i, j)

print(max_ans)

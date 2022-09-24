# 가는 방향이 오른과 밑으로 가니까 
import sys

input = sys.stdin.readline

# 홀,짝 열별로
_even = [(-1, 1), (0, 1), (1, 0)]
_odd = [(0, 1), (1, 1), (1, 0)]

N, M = map(int, input().split())
K = int(input())
hole = []
for _ in range(K):
    x, y = map(int, input().split())
    hole.append((x - 1, y - 1))

bees = [[0] * M for _ in range(N)]
bees[0][0] = 1
for i in range(K):
    bees[hole[i][0]][hole[i][1]] = -1  # 구멍체크

for k in range(M):
    for j in range(N):
        if bees[j][k] != -1:
            if k % 2 == 0:  # 짝
                for l in range(3):
                    nr = j + _even[l][0]
                    nc = k + _even[l][1]
                    if 0 <= nr < N and 0 <= nc < M and bees[nr][nc] != -1:
                        bees[nr][nc] += bees[j][k]
            else:
                for m in range(3):
                    nr = j + _odd[m][0]
                    nc = k + _odd[m][1]
                    if 0 <= nr < N and 0 <= nc < M and bees[nr][nc] != -1:
                        bees[nr][nc] += bees[j][k]
print((bees[-1][-1]) % 1000000007)

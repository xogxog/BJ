# 삼성문제는 heapq 안나온다. 괜히 쓰지말자..
# enumerate 자주 사용하자 존나 유용하다.
import sys

dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

input = sys.stdin.readline
N, M, K = map(int, input().split())  # 땅크기, 나무 갯수, 년

A = [[5] * N for _ in range(N)]  # 상도 땅
food = []  # 양분
for _ in range(N):
    tmp = list(map(int, input().split()))
    food.append(tmp)

trees = [[[] for i in range(N)] for j in range(N)]

for k in range(M):
    x, y, z = map(int, input().split())
    trees[x - 1][y - 1].append(z)

for l in range(K):
    for m in range(N):
        for n in range(N):
            # 봄
            trees[m][n].sort()
            dead_t = []
            for idx, now_tree in enumerate(trees[m][n]):
                if A[m][n] >= now_tree:  # 양분 먹을 수 있으면
                    trees[m][n][idx] += 1  # 나이 +1
                    A[m][n] -= now_tree  # 양분 - tree 만큼
                else:  # 양분 못먹어서 죽는 나무
                    dead_t = trees[m][n][idx:]
                    trees[m][n] = trees[m][n][:idx]
                    break

            # 여름
            for q in range(len(dead_t)):
                A[m][n] += dead_t[q] // 2

            # 겨울
            A[m][n] += food[m][n]

    # 가을
    for _m in range(N):
        for _n in range(N):
            for tree_age in trees[_m][_n]:
                if tree_age % 5 == 0:
                    for _i in range(8):
                        nr = _m + dr[_i]
                        nc = _n + dc[_i]
                        if 0 <= nr < N and 0 <= nc < N:  # 인접칸에 나무 생김
                            trees[nr][nc].append(1)

ans = 0
for _p in range(N):
    for _q in range(N):
        ans += len(trees[_p][_q])
print(ans)

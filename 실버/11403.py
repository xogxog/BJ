import sys
input = sys.stdin.readline
N = int(input())
ls=[list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N) :
        for k in range(len(ls[j])) :
            if ls[j][i] and ls[i][k] :
                ls[j][k] = 1

for _ in range(N) :
    print(*ls[_])

# visited= copy.deepcopy(ls)
# for i in range(N) :
#     for j in range(N):
#         if ls[i][j] :
#             for k in range(N) :
#                 if ls[j+1][k] == 1:
#                     visited[i][k] = 1
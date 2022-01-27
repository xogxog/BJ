N,M = map(int,input().split()) # r, c

ls = [list(map(int,input().split())) for _ in range(N)]
# 동 남 서 북
dr = [0,1,0,-1]
dc = [1,0,-1,0]

pieces = [
    [[0,1,2]],
    [
        [0,0,0],
        [1,1,1]
    ],
    [
        [1,1,0],
        [2,2,1],
        [3,3,2],
        [0,0,3],
        [1,1,2],
        [2,2,3],
        [3,3,0],
        [0,0,1]
    ],
    [
        [1,0,1],
        [2,1,2],
        [1,2,1],
        [0,1,0]
    ],
    [
        [0,1,2],
        [1,2,3],
        [0,1,3],
        [0,2,3]
    ]
]
max_total = 0
for i in range(N) :
    for j in range(M) :
        for k in range(len(pieces)) :
            for l in range(len(pieces[k])) :
                r = i
                c = j
                flag = 0
                tmp_total = ls[i][j]
                for m in range(len(pieces[k][l])) :
                    nr = r+dr[pieces[k][l][m]]
                    nc = c + dc[pieces[k][l][m]]

                    if 0<=nr<N and 0<=nc<M :
                        tmp_total += ls[nr][nc]

                    else :
                        flag = 1
                        break
                    if k != 4 :
                        r, c = nr, nc
                if flag == 0 :
                    if max_total < tmp_total :
                        max_total = tmp_total
print(max_total)
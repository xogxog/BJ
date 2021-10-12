# 2806. N-Queen

dr = [1,1]
dc = [1,-1]


def queen(chess, depth) :
    global cnt
    for i in range(N) :
        if visited[i] == 0 and chess[depth][i] == 0 : # 방문하지 않았고 ,체스판에 둘수 있으면
            chess[depth][i] = 1                               # 체스판에 체스를 둔다.
            visited[i] = 1

            if depth == N-1 :                            # 끝까지 왔다는 것은..! 성공했단 것이므로
                cnt += 1

            for j in range(2) :
                mr = depth + dr[j]
                mc = i + dc[j]
                while 0<=mr<N and 0<=mc<N :
                    chess[mr][mc] = chess[mr][mc] +1
                    mr = mr + dr[j]
                    mc = mc + dc[j]
            queen(chess, depth+1)
        else :
            continue
        visited[i] = 0
        chess[depth][i] = 0
        for k in range(2) :
            mr = depth + dr[k]
            mc = i + dc[k]
            while 0<=mr<N and 0<=mc<N :
                chess[mr][mc] = chess[mr][mc] -1
                mr = mr + dr[k]
                mc = mc + dc[k]



N = int(input())

chess = [[0] * N for _ in range(N)]
visited = [0] * N # 열 체크해서 해당 열에 가지 못하도록
cnt = 0

queen(chess, 0)
print(cnt)
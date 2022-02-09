def check(tmp,idx):
    global ans
    if idx == N :
        if tmp < ans :
            ans = tmp
        return

    if tmp > ans :
        return

    for i in range(idx,N):
        for j in range(3):
            if not visited[i][j] :
                visited[i][j] = 1
                color[i] = j
                check(tmp+ls[i][j],idx+1)
                visited[i][j] = 0
                color[i] = 0


N = int(input())
ls=[list(map(int,input().split())) for _ in range(N)]
visited = [[0]*3 for _ in range(N)]
color = [-1]*N
ans = 987654321
idx=0
check(0,idx)
print(ans)

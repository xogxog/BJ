def bridge(ls) :
    global ans
    visited = [[0] * N for _ in range(N)]

    for i in range(N) :
        r = 0
        while True :
            if r == N-1 : # 다리 건넌 경우
                ans += 1
                break
            if ls[i][r] == ls[i][r+1] : # 높이가 같은 경우 건너기
                r += 1
            elif ls[i][r] -ls[i][r+1] == 1 and r+L+1 <= N and ls[i][r+1 : r+1+L].count(ls[i][r+1])==L and visited[i][r+1 : r+1+L].count(0)==L: # 놓을수 있는 곳 높이 같고,다리를 놓을 수 있는 범위,다리 놓았는지 여부 판단
                tmp = 1
                while tmp < L+1 : # 다리 놓음
                    visited[i][r+tmp] = 1
                    tmp += 1
                r += L # 다리 놓은 곳 이동
            elif ls[i][r] -ls[i][r+1] == -1 and r-L+1 >= 0 and ls[i][r+1-L:r+1].count(ls[i][r])==L and visited[i][r+1-L:r+1].count(0)==L :
                tmp = r+1-L
                while tmp < r+1:  # 다리 놓음
                    visited[i][tmp] = 1
                    tmp += 1
                r += 1 # 다음으로 이동
            else :
                break





N,L = map(int,input().split())

ls = [list(map(int,input().split())) for _ in range(N)]
ls2 = list(map(list,zip(*ls))) # 90도 돌리기
ans = 0
bridge(ls)
bridge(ls2)
print(ans)

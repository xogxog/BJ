import sys
input = sys.stdin.readline

t,w = map(int,input().split()) # 초, 움직이는 횟수(짝수-> 1번나무에 있음, 홀수 -> 2번나무)
ls = [int(input()) for _ in range(t)]
dp = [[0]*(w+1) for _ in range(t)]

for i in range(t) :
    for j in range(w+1) :
        if j == 0 : # 계속 안움직이는 경우, 1에서만 점수가 오름
            if ls[i] == 1 : # i 초일때 1번 나무
                dp[i][0] = dp[i-1][0] + 1
            else :
                dp[i][0] = dp[i-1][0]

        else :
            if j % 2 == 0 and ls[i] == 1 : #1번나무 먹음
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-1])+1
            elif j%2 and ls[i] == 2 : # 2번나무 먹음
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-1])+1
            else : #못먹음
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-1])

print(max(dp[-1]))
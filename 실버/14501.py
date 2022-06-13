# dp - 거꾸로 생각하기 어렵다 ...
import sys
input = sys.stdin.readline


N = int(input())
ls = []
for _ in range(N) :
    ls.append(tuple(map(int,input().split())))

dp = [0] * (N+1)

for i in range(N-1,-1,-1) :
    if ls[i][0] + i > N : # 일이 끝나고 난 후이므로 일 할 수 없음
        dp[i] = dp[i+1]
    else :
        # print(ls[i][1]+dp[i+ls[i][0]],dp[i+1])
        dp[i] = max(ls[i][1]+dp[i+ls[i][0]], dp[i+1]) # 당일 일 + 상담끝나고 날 수익 or 다음날 금액
        # print(dp)

print(dp[0])

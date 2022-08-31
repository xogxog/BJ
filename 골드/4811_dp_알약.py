import sys
input = sys.stdin.readline

dp = [[0]*31 for _ in range(31)]

for w in range(31):
    for h in range(31):
        if h>w: # w 개수보다 h 개수가 많아질수없음
            continue
        if h == 0 : # 쪼개지는 알약 X
            dp[w][h] = 1
        else :
            dp[w][h] = dp[w-1][h]+dp[w][h-1]

medi = int(input())

while medi :
    print(dp[medi][medi])
    medi = int(input())
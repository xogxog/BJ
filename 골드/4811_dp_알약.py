import sys
input = sys.stdin.readline

dp = [[0]*5 for _ in range(5)]

for w in range(5):
    for h in range(5):
        if h>w: # w 개수보다 h 개수가 많아질수없음
            continue
        if h == 0 : # 쪼개지는 알약 X
            dp[w][h] = 1
        else :
            dp[w][h] = dp[w-1][h]+dp[w][h-1]
    print(f'=======')
    for z in range(5):
        print(*dp[z])

medi = int(input())

while medi :
    print(dp[medi][medi])
    medi = int(input())
import sys
input = sys.stdin.readline
n = int(input())
# wine = list(int(input()) for _ in range(n))
# 런타임 에러 ,...
# def drink(idx, mount, cnt) :
#     global ans
#     if idx >= n :
#         if mount > ans :
#             ans = mount
#         return
#     if cnt == 2 :
#         drink(idx+1,mount,0)
#     else :
#         drink(idx+1,mount+wine[idx],cnt+1) # 연속으로 마시기
#         drink(idx+1, mount, cnt) # 연속으로 안마시기
# ans = 0
#
# drink(1,wine[0],1)
# drink(1,0,0)
# print(ans)

wines = [0] + list(int(input()) for _ in range(n)) + [0]

dp = [0] *(n+2)
dp[1] = wines[1]
dp[2] = dp[1]+wines[2]

for i in range(3,n+1) :
    dp[i] = max(dp[i-3]+wines[i-1]+wines[i], dp[i-2]+wines[i], dp[i-1])
print(dp[n])

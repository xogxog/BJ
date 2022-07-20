import sys
input = sys.stdin.readline

N = int(input()) # 객차 수
train = [0] + list(map(int,input().split()))
m = int(input()) # 끌 수 있는 최대 객차 수
dp = [[0 for i in range(N+1)] for _ in range(3)]
accu_ls = [0 for j in range(N+1)] # 누적합 리스트

for k in range(1,N+1) :
    accu_ls[k] = accu_ls[k-1] + train[k]

for l in range(3) :
    for n in range((l+1)*m,N+1):
        if l == 0 :
            dp[l][n] = max(dp[l][n-1], accu_ls[n]-accu_ls[n-m]) # 현재값 포함X 최댓값, 현재칸 포함한 경우

        else :
            dp[l][n] = max(dp[l][n-1],(dp[l-1][n-m]+accu_ls[n]-accu_ls[n-m]))

print(dp[-1][-1])
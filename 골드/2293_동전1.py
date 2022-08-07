import sys

input = sys.stdin.readline

n,k = map(int,input().split())

coins = list(int(input()) for _ in range(n))
ans = [0]*(k+1)
ans[0] = 1

for coin in coins :
    for i in range(coin,k+1):
        ans[i] += ans[i-coin]
print(ans[-1])
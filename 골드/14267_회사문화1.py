import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
employee = list(map(int, input().split()))

adj = [set() for _ in range(n+1)]
tmp = [0]*(n+1)
dp = [0]*(n+1)
for i in range(1, n):
    adj[employee[i]].add(i+1)  # 단방향

for _ in range(m):
    emp, w = map(int, input().split())
    tmp[emp] += w

for i in range(2, n+1):
    if tmp[i]:
        q = deque([i])  # 상사 넣기
        w = tmp[i]
        dp[i] += w
        while q:
            node = q.popleft()
            for j in adj[node]:
                q.append(j)
                dp[j] += w

print(*dp[1:])

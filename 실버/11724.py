import sys
from collections import deque
input = sys.stdin.readline

def my_graph(q) :
    while q :
        now = q.popleft()
        for i in adj_ls[now] :
            if not visited[i]:
                q.append(i)
                visited[i] = 1

N,M = map(int,input().split())
adj_ls = [[] for _ in range(N+1)]
for _ in range(M) :
    a,b = map(int,input().split())
    adj_ls[a].append(b)
    adj_ls[b].append(a)

visited = [0] * (N+1)
cnt = 0
visited[0] = 1
q = deque()
for _i in range(1,N+1) :
    if not visited[_i] :
        visited[_i] = 1
        q.append(_i)
        my_graph(q)
        cnt += 1

print(cnt)
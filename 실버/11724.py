import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
adj_ls = [[] for _ in range(N+1)]
for _ in range(M) :
    a,b = map(int,input().split())
    adj_ls[a].append(b)
    adj_ls[b].append(a)

visited = [0] * (N+1)
cnt = 0
visited[0] = 1
visited[1] = 1
q = deque()
q.append(1)
flag = 1
while flag :
    while q :
        now = q.popleft()
        for i in adj_ls[now] :
            if not visited[i]:
                q.append(i)
                visited[i] = 1

    cnt +=1
    try :
        q.append(visited.index(0))
    except :
        flag = 0
        pass
print(cnt)
from collections import deque
def dfs(V) :
    if sum(visited1) == len(visited1)-1 :
        return
    for j in adj_ls[V] :

        if not visited1[j] :
            visited1[j] = 1
            ans1.append(j)
            dfs(j)

def bfs(V) :
    q = deque()
    q.append(V)

    while q :

        curr = q.popleft()

        for k in adj_ls[curr] :
            if not visited2[k] :
                visited2[k] = 1
                q.append(k)
                ans2.append(k)

N,M,V = map(int,input().split())

adj_ls = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int,input().split())

    adj_ls[a].append(b)
    adj_ls[b].append(a)

for i in range(len(adj_ls)):
    adj_ls[i].sort()

visited1=[0]*(N+1)
visited1[V]=1
ans1=[V]
dfs(V)
print(*ans1)

visited2=[0]*(N+1)
visited2[V]=1
ans2=[V]
bfs(V)
print(*ans2)
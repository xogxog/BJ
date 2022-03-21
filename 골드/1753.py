import sys
from collections import deque
import heapq

input = sys.stdin.readline
V,E = map(int,input().split()) # 정점, 간선 개수
k = int(input()) # 시작 정점 번호/ 시작 1부터

visited = [987654321]*(V+1)
adj_ls = [[] for _ in range(V+1)]
q = deque()
for _ in range(E):
    u,v,w = map(int,input().split())
    adj_ls[u].append((u,v,w))
    if u == k :
        q.append((u,v,w))

visited[k]=0
# print(adj_ls)
while q :
    u, v, w = q.popleft()

    if visited[u] + w < visited[v] :
        visited[v] = visited[u]+w
        for node in adj_ls[v] :
            if visited[v] + node[2] < visited[node[1]] :
                q.append(node)

for i in range(1, V+1) :
    if visited[i] == 987654321 :
        print('INF')
    else :
        print(visited[i])
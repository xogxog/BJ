import sys
from collections import deque

input = sys.stdin.readline
V,E = map(int,input().split()) # 정점, 간선 개수
k = int(input()) # 시작 정점 번호/ 시작 1부터

visited = [987654321]*(V+1)
adj_ls = [{} for _ in range(V+1)] # [{}, {}, {}]
q = deque()
for _ in range(E):
    u,v,w = map(int,input().split())
    if v not in adj_ls[u] :
        adj_ls[u][v] = w
    else :
        adj_ls[u][v] = min(adj_ls[u][v],w)


q.append(k)

visited[k]=0
# print(adj_ls)
while q :
    _start = q.popleft()
    for _end,_wei in adj_ls[_start].items():
        if visited[_start] + _wei < visited[_end] :
            visited[_end] = visited[_start]+_wei
            q.append(_end)

# for i in range(1, V+1) :
#     if visited[i] == 987654321 :
#         print('INF')
#     else :
#         print(visited[i])
for i in range(1,V+1):
    if visited[i] == 987654321 :
        sys.stdout.write("INF")
    else :
        sys.stdout.write(str(visited[i])+'\n')
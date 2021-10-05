from collections import deque
N = int(input()) # 컴퓨터 갯수
E = int(input()) # 노드 연결 수


adj_list = [[] for _ in range(N+1)]
visited = [0] *(N+1)

for i in range(E) :
    st, ed = map(int, input().split())
    adj_list[st].append(ed) # 여기서 멈추면 방향성이 있음.
    adj_list[ed].append(st)


q= deque()
visited[1] = 1

for j in range(len(adj_list[1])) :
    q.append(adj_list[1][j])

while q :
    idx = q.popleft()
    visited[idx] = 1
    for k in range(len(adj_list[idx])) :
        if visited[adj_list[idx][k]] == 0 :
            visited[adj_list[idx][k]] = 1
            q.append(adj_list[idx][k])

print(visited.count(1)-1)
import sys
from collections import deque

def my_graph() :
    # deque 생성 및 visited 리스트 / 시작점 1로두고 visited, q에 각 넣어주기
    q = deque()
    group = 1
    flag = True
    for i in range(1,V+1): # 연결이 안된 노드들도 전부 검사해주기위한 loop
        if visited[i] == 0:
            q.append(i)
            visited[i] = group
            while q:
                v = q.popleft()

                for j in range(len(graph[v])):
                    if visited[graph[v][j]] == 0:  # 방문하지 않았으면
                        visited[graph[v][j]] = -1 * visited[v]
                        q.append(graph[v][j])
                    elif visited[graph[v][j]] != 0 and visited[v] == visited[graph[v][j]]:  # 현재의 visit과 연결된 노드의 visit이 같다면
                        flag = False

    return ('YES' if flag == True else 'NO')

for _ in range(1, int(sys.stdin.readline().rstrip())+1) :
    V, E = map(int,sys.stdin.readline().split())
    graph = [[] for _ in range(V+1)] # 빈그래프
    visited = [0] * (V+1) # 정점은 1부터시작이므로

    for i in range(E) :
        p, c = map(int, sys.stdin.readline().split())
        graph[p].append(c)
        graph[c].append(p) # 양방향 그래프

    print(my_graph())


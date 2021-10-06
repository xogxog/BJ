# 로직은 간단하나, 이 로직의 아이디어를 떠올리는게 힘들다..!
# 아이디어 : 현재위치에서 -1, +1, *2 가면 그전 이동횟수+1 / 단 한번 방문했던 곳은 방문 X
# 왜냐하면 나중에 다시 방문한다는게 최소경로가 아니므로 .
from collections import deque
def bfs() :
    q = deque()
    q.append(start)
    visited[start] = 1

    while q :
        go = q.popleft()
        if go == end :
            return
        if 0<=go-1<N and visited[go-1] == 0 :
            visited[go-1] = visited[go] + 1
            q.append(go-1)
        if 0<=go+1<N and visited[go+1] == 0 :
            visited[go + 1] = visited[go] + 1
            q.append(go+1)
        if 0<=go*2<N and visited[go*2] == 0 :
            visited[go*2] = visited[go] + 1
            q.append(go*2)




start, end = map(int,input().split())
N = 200000 # 이 범위 잘못 잡아서 런타임 에러 났다
visited = [0] * N

bfs()

print(visited[end]-1)
# 네트워크 복구
# 다익스트라
# 힙큐로도 풀어보기
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
ls =[[]*(N+1) for _ in range(N+1)]
road = [[]*(N+1) for _ in range(N+1)] # 가는 곳 적어둘 리스트
set_road = set()

def dijkstra() :
    dist = [987654321] * (N+1)
    visited = [0] * (N+1)

    dist[1] = 0 # 슈퍼컴퓨터~

    for _ in range(1,N+1) : # 모든 정점 돌거임
        min_idx = -1
        min_value = 987654321

        # 가장 최소 인덱스 찾기
        for i in range(1, N+1):
            if not visited[i] and dist[i] < min_value :
                min_idx = i
                min_value = dist[i]

        visited[min_idx] = 1
        for k in range(0,len(road[min_idx]),2) :
            set_road.add((road[min_idx][k],road[min_idx][k+1]))

        for next in ls[min_idx]: # next[0] : 연결된 노드, next[1] : 연결된 노드 가중치
            # 2차원으로 하면 visited check해주는데 여기선 안해도 되나 ,, ?
            w = dist[min_idx] + next[1] # 연결된 노드 가중치 계산
            if  dist[next[0]] > w :
                dist[next[0]] = w
                road[next[0]] = road[min_idx] + [min_idx, next[0]]







for _ in range(M):
    a,b,c = map(int,input().split())
    ls[a].append((b,c))
    ls[b].append((a,c))


dijkstra()

print(len(set_road))
for x,y in set_road :
    print(x,y)
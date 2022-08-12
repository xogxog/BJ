import sys
import heapq

input = sys.stdin.readline

def dijkstra(start) :
    q = []
    heapq.heappush(q,(0,start)) #  시작지점 넣어주기
    distance = [INF] * (V+1)
    distance[start] = 0

    while q :
        dist, curr_node = heapq.heappop(q) # 거리, 현재 노드

        if distance[curr_node] < dist :
            continue

        for next, w in ls[curr_node] :
            cost = dist+w
            if cost < distance[next] :
                distance[next] = cost
                heapq.heappush(q,(cost, next))

    return distance
V,E = map(int,input().split()) # 정점, 간선 개수
k = int(input()) # 시작 정점 번호/ 시작 1부터
INF = 987654321

ls = [[] for _ in range(V+1)]

for _ in range(E):
    u,v,w = map(int,input().split())
    ls[u].append((v,w)) # 노드, 가중치


ans = dijkstra(k)

for i in range(1,V+1) :
    if ans[i] == 987654321 :
        print('INF')
    else :
        print(ans[i])
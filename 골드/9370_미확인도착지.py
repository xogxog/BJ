import sys
import heapq

input = sys.stdin.readline

def dijkstra(start) :

    q = []
    heapq.heappush(q,(0,start)) # 시작지점 넣어주기
    distance = [inf] * (N + 1)
    distance[start] = 0

    while q :
        dist, curr_node = heapq.heappop(q) # 거리, 현재노드

        if distance[curr_node] < dist : # 이미 노드가 최적의 길이를 가지고 있다면 pass
            continue

        for next_node,w in road[curr_node] :
            cost = dist + w
            if cost < distance[next_node] :
                distance[next_node] = cost
                heapq.heappush(q,(cost, next_node)) # 여기서 누적된 cost를 넣어줘야한다 !


    return distance


for tc in range(int(input())) :

    N,M,T = map(int,input().split()) # 교차로, 도로, 목적지 후보의 개수

    S,G,H = map(int,input().split()) # 예술가들 출발지, g와 h 교차로 사이에 있는 도로 지나감

    road = [[] for _ in range(N+1)]

    for _ in range(M):
        a,b,d = map(int,input().split())
        road[a].append((b,d)) # 노드, 가중치
        road[b].append((a,d))

    inf = 987654321

    ans = []
    arrive_points = [int(input()) for _ in range(T)]

    _start = dijkstra(S)
    _G = dijkstra(G)
    _H = dijkstra(H)

    for arrived in arrive_points :
        if _start[G] + _G[H] + _H[arrived] == _start[arrived] or _start[H] + _H[G] + _G[arrived] == _start[arrived] :
            ans.append(arrived)
    ans.sort()
    print(' '.join(map(str,ans)))
# 성우 코드 보기

import sys
import heapq
input = sys.stdin.readline

G = int(input()) # 게이트 수
P = int(input()) # 비행기의 수


# union 방법


parent = [0] * (G+1)
ans = 0
for i in range(1,G+1) :
    parent[i]=i
flights = []
for _ in range(P) :
    flights.append(int(input()))

# 해당 번호의 부모가 1~i까지 도킹되지 않은 가장 큰 게이트 번호를 갖는 번호
def find(x) :
    if parent[x] == x : # 도킹 되지 않은 곳!
        return x
    parent[x] = find(parent[x]) # 부모테이블에 바로 갱신
    return parent[x]

for flight in flights :
    docking = find(flight)
    print(parent)
    if docking ==  0 :
        break
    parent[docking] = parent[docking-1]
    ans += 1
print(ans)


# 시간초과
# jari = [1]+[0]*G
# flag = 0
# for _ in range(P) :
#     flight_num = int(input())
#     for i in range(flight_num,-1,-1) :
#         if jari[i] == 0 :
#             jari[i] = 1
#             break
#         elif i == 0 :
#             flag = 1
#             break
#     if flag :
#         break
# print(sum(jari)-1)

# 힙큐 시간초과

# heap = []
# for i in range(G+1) : # 게이트 만큼 최대힙 넣어주기
#     heapq.heappush(heap, -i)
#
# ans = 0
# flights = []
# for _ in range(P) :
#     flights.append(int(input()))
# flag = 0
# for flight in flights :
#     tmp_h_ls = []
#     while 1 :
#         tmp_h = heapq.heappop(heap)
#         if tmp_h != 0 and -tmp_h <= flight :
#             ans += 1
#             break
#         elif tmp_h == 0 :
#             flag = 1
#             break
#         else :
#             tmp_h_ls.append(tmp_h)
#     if flag :
#         break
#     for tmp_h_i in tmp_h_ls :
#         heapq.heappush(heap, tmp_h_i)
#
# print(ans)

# 성우코드
import sys

input = sys.stdin.readline


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


g = int(input())
p = int(input())

parent = [x for x in range(g + 1)]

ans = 0
closed = False
for _ in range(p):
    gi = int(input())
    if not closed:
        x = find(gi)
        if x == 0:
            closed = True
            break
        else:
            union(x, x - 1)
            ans += 1
print(ans)

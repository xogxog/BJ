import sys
input = sys.stdin.readline

G = int(input()) # 게이트 수
P = int(input()) # 비행기의 수
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
    parent[x] = find(parent[x])
    return parent[x]

for flight in flights :
    docking = find(flight)
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

# union-find


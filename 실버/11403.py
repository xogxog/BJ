from collections import deque
N = int(input())
ls=[set() for _ in range(N)]
visited = [[0]*N for _ in range(N)]

for i in range(N):
    tmp = list(map(int,input().split()))
    for j in range(N) :
        if tmp[j] == 1:
            ls[i].add(j)
            ls[j].add(i)
print(ls)


for i in range(N):
    q = deque(ls[i])
    while q :
        connect = q.popleft()

        if not visited[i][connect] :
            visited[i][connect] = 1
            print(f'i 번째 visited : {visited[i]}')
            print(f'i : {i}, connect : {connect}')
            if i != connect :
                for j in range(len(ls[connect])) :
                    print(j)
                    if ls[connect][j] and not visited[i][ls[connect][j]] :
                        q.append(ls[connect][j])
                        print(i, ls[connect][j])
                        print(q)
                        # print(visited)

print(visited)

# visited= copy.deepcopy(ls)
# for i in range(N) :
#     for j in range(N):
#         if ls[i][j] :
#             for k in range(N) :
#                 if ls[j+1][k] == 1:
#                     visited[i][k] = 1
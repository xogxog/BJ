from collections import deque

N,M = map(int,input().split())
ls = [[] for _ in range(N+1)]
max_num=0
hacking_computer=[0]*(N+1)
ans =[0]*(N+1)
for _ in range(M):
    a,b= map(int,input().split())
    ls[b].append(a) #b는 a에 신뢰받음

for i in range(1,N+1) :
    visited = [0]*(N+1)
    visited[i] = 1
    q = deque()
    q.append(i)
    cnt = 0
    while q :
        curr = q.popleft()

        for l in range(len(ls[curr])) :
            if not visited[ls[curr][l]] :
                visited[ls[curr][l]] = 1
                cnt += 1
                q.append(ls[curr][l])
    ans[i] = cnt


anss =[]
for j in range(1,N+1) :
    if ans[j] == max(ans) :
        anss.append(j)

print(*anss)
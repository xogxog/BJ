import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def find(x) :
    if x != parent[x] :
        parent[x] = find(parent[x])
    return parent[x]


def union(a,b) :
    a = find(a)
    b = find(b)

    if a < b :
        parent[b] = a
    else :
        parent[a] = b

def bfs(idx):
    global ls
    visited = [0] * (N+1)
    visited[idx] = 1

    q = deque()
    q.append([idx,0])
    tmp_max = 0
    while q :
        now, cnt = q.popleft()
        if tmp_max < cnt :
            tmp_max = cnt
        for i in range(len(ls[now])) :
            if not visited[ls[now][i]] :
                visited[ls[now][i]] = 1
                q.append([ls[now][i],cnt+1])

    return tmp_max


N = int(input()) # 회의 참석하는 사람의 수
M = int(input())
parent = [i for i in range(N+1)]
ls = [[] for _ in range(N+1)]


for _ in range(M) :
    a,b = map(int,input().split())
    union(a,b)
    ls[a].append(b)
    ls[b].append(a)

for k in range(1,len(parent)) :
    parent[k] = find(k)

max_dict = defaultdict()
for j in range(1,N+1) :
    cnt = bfs(j)
    max_dict[j] = [parent[j],cnt]
# print(max_dict)

ans_dic = defaultdict(lambda : [0,987654321]) # 노드, 최댓값

for key,value in max_dict.items() : # key : 노드 , value : [부모, 거리]
    if ans_dic[value[0]][1] > value[1] :
        ans_dic[value[0]] = [key,value[1]]
# print(ans_dic)

ans_ls = []
for key2, value2 in ans_dic.items() :
    ans_ls.append(value2[0])

print(len(ans_ls))
ans_ls.sort()
for z in ans_ls :
    print(z)
import sys
from collections import defaultdict
input = sys.stdin.readline

def find(x) :
    if x != parent[x] :
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b) :
    a = find(a)
    b = find(b)

    if parent[a] != parent[b] : # a의 대표에다가 추가 , 친구들도 a로 누적합시키기
        parent[b] = a
        cnt[a] += cnt[b]


    


for _ in range(int(input())) :
    F = int(input())

    parent = {} # 친구 연결
    cnt = {} # 각 사람별 친구 수 누적해줄 dictionary

    for _ in range(F) :
        a,b = input().split()

        if a not in cnt :
            cnt[a] = 1
            parent[a] = a
        if b not in cnt :
            cnt[b] = 1
            parent[b] = b

        union(a,b)

        print(cnt[find(a)]) # a의 대표에다가 합쳤으니까







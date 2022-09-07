import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

for _ in range(int(input())) :
    n,S = map(int,input().split()) # 숙제 갯수, 현재시각
    t = list(map(int,input().split())) # 숙제나오는 시간
    v = list(map(int,input().split())) # 벌점

    ans = 0

    heap = []
    for i in range(n):
        heapq.heappush(heap,(-v[i],t[i])) # 벌점기준 최대힙

    check = set()
    min_t = S

    while heap :
        now_v, now_t = heapq.heappop(heap)

        # 내가 현재최소로 제출할수있는 시간보다 now_t가 크다면
        if min_t < now_t :
            if now_t not in check :
                check.add(now_t)
            else :
                submit = now_t
                while submit in check :
                    submit += 1
                check.add(submit)
                ans += (submit-now_t)*(-1*now_v)
        else :
            if min_t not in check :
                pass
            else :
                while min_t in check :
                    min_t += 1
            ans += (min_t-now_t)*(-1*now_v)
            check.add(min_t)
            min_t += 1

    print(ans)

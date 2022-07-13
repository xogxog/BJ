# 과제
# 그리디, 우선순위 큐

# 웅찬이는 과제가 많다. 하루에 한 과제를 끝낼 수 있는데, 과제마다 마감일이 있으므로 모든 과제를 끝내지 못할 수도 있다.
# 과제마다 끝냈을 때 얻을 수 있는 점수가 있는데, 마감일이 지난 과제는 점수를 받을 수 없다.
#
# 웅찬이는 가장 점수를 많이 받을 수 있도록 과제를 수행하고 싶다. 웅찬이를 도와 얻을 수 있는 점수의 최댓값을 구하시오.

import sys
from heapq import heappush, heappop

input = sys.stdin.readline
N = int(input())

work = []
max_d = 0
for _ in range(N) :
    d,w = map(int,input().split())
    if max_d < d :
        max_d = d
    heappush(work, (-d, -w))

ans = 0

for idx in range(max_d-1,-1,-1):
    tmp_work_ls = []
    while work :
        d,w = heappop(work)
        if -d > idx : # 기한 날짜가 지나지 않은 것들만 뽑는다.
            heappush(tmp_work_ls, (w,d)) # 정렬기준은 w
        else :
            heappush(work, (d,w))
            break
    if len(tmp_work_ls) : # 기한날짜 지나지 않고, 가장 큰값이 있는 경우
        ans += -heappop(tmp_work_ls)[0]

        for j in range(len(tmp_work_ls)) :
            w,d = heappop(tmp_work_ls)
            heappush(work, (d,w))

print(ans)
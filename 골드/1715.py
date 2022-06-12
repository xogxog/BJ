# 힙큐, 우선순위 큐!!
import sys
import heapq

input = sys.stdin.readline
ans = 0
N = int(input())
cards =[]
for _ in range(N) :
    heapq.heappush(cards,int(input().rstrip()))


if len(cards) == 1 :
    print(0)
else :
    while len(cards) >1:
        tmp_sum = heapq.heappop(cards) + heapq.heappop(cards)
        ans += tmp_sum
        heapq.heappush(cards,tmp_sum)
    print(ans)
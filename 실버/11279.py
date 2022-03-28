# 최대 힙
import sys
import heapq
input = sys.stdin.readline
h = []
for _ in range(int(input())):
    num = int(input())
    if num == 0 :
        if len(h) > 0 :
            print(heapq.heappop(h)[1]) # 원래값 출력 위해 [1]
        else :
            print(0)
    else :
        heapq.heappush(h,[-num,num])
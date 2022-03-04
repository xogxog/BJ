# 이분탐색
import sys
input = sys.stdin.readline
N,M = map(int,input().split()) # 나무의 수, 가져가는 나무의 길이
trees = list(map(int,input().split()))
low=0
high = max(trees)
while low < high :
    mid = (low+high+1)//2
    tot = 0
    for tree in trees :
        if tree > mid : # 나무 > 토막낼 높이
            tot += tree - mid
    # print(low, mid, high)
    if tot < M : # 가져갈 길이가 작으면 높이 낮추기
        high=mid -1
    else : # 가져갈 길이가 같거나 크면
        low=mid

print(low)

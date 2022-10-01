import sys
input = sys.stdin.readline

n, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

start, end = 0, arr[-1]-arr[0]
cnt = 1  # 가장앞부분은 공유기 심었다고 가정
while start <= end:
    mid = (start+end)//2

    for i in range(n):
        if arr[i] >=

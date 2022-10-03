import sys
input = sys.stdin.readline

n = int(input())
city = list(map(int, input().split()))
m = int(input())

start, end = 1, max(city)  # 줄 수 있는 금액 범위
ans = 0
while start <= end:
    mid = (start+end) // 2
    amt = 0

    for c in city:
        amt += min(c, mid)

    if amt <= m:
        start = mid+1
        ans = mid
    else:
        end = mid-1

print(ans)

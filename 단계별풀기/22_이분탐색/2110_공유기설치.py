import sys
input = sys.stdin.readline

n, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

start, end = 1, arr[-1]-arr[0]  # 최소거리, 최대거리
ans = 0
while start <= end:
    mid = (start+end)//2  # 가장 클 수 있는 거리의 중간값
    curr = arr[0]  # 첫번째 공유기부터
    cnt = 1  # 가장앞부분은 공유기 심었다고 가정
    for i in range(1, n):
        if arr[i] >= curr + mid:
            curr = arr[i]  # 공유기 심기 -> 갱신해줘야 다음 공유기와의 거리를 잴수 있다.
            cnt += 1

    if cnt >= c:
        start = mid + 1  # 거리 넓히기
        ans = mid  # mid = 간격
    else:
        end = mid - 1

print(ans)

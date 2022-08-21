import sys, heapq

# 입력부
tc = int(sys.stdin.readline())
for _ in range(tc):
    n, m = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))

    # empty : 현재 호수가 비었는지 아닌지를 저장하는 리스트
    empty = [False] * (n + 1)
    # can : 재앙을 피할 수 있는지 없는지 나타내는 flag 변수
    can = True
    # cache : 현재 호수 번호가 i일 때, 비가 오는 시간을 역순으로 저장하는 2차원 배열
    cache = [[] for _ in range(n + 1)]
    # time : 현재 시간 i에서 비가 올 때 해당하는 호수의 번호
    time = [-1] * m
    for i in range(m - 1, -1, -1):
        if arr[i]:
            time[i] = arr[i]
            cache[arr[i]].append(i)
    print(cache)
    # 가장 첫 시간을 우선순위 큐에 삽입
    q = []
    for i in range(1, n + 1):
        if cache[i]:
            heapq.heappush(q, cache[i].pop())
    print(q)
    # ans : 용이 마시는 호수 번호를 저장하는 리스트
    ans = []
    for i in range(m):
        # 현재 비가 온다면
        if arr[i]:
            # 비가 오는데 호수가 비지 않으면 재앙이 일어남
            if not empty[arr[i]]:
                can = False
                break
            # 비가 오는데 호수가 비었다면 그 다음 비오는 시간을 우선순위 큐에 저장
            empty[arr[i]] = False
            if cache[arr[i]]:
                heapq.heappush(q, cache[arr[i]].pop())

        # 비가 오지 않는다면
        else:
            # 마실 수 있는 호수가 있다면 그리디하게 마신다
            if q:
                now = q[0]
                heapq.heappop(q)
                ans.append(time[now])
                empty[time[now]] = True
            # 마실 수 있는 호수가 없으니 0을 저장한다
            else:
                ans.append(0)

    # 정답 출력
    if not can:
        print('NO')
    else:
        print('YES')
        print(' '.join(map(str, ans)))




# import sys
# input = sys.stdin.readline
# from collections import defaultdict
# for _ in range(int(input())) :
#     n,m = map(int,input().split()) # 호수 갯수, 호수 비내리는 날의 수
#     ls = list(map(int,input().split())) # 비 언제오는지
#     water = [1] * (n+1) # 비어있는지 check
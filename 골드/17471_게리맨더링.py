# 함수안에서 global변수를 건드는 것은 좋지 않다.
# 함수의 반환값으로 ans를 주고 밖에서 할당해주는게 훨씬 좋다.
# 공쥬풀이 : shift 연산으로 먼저 구역을 나누고 이어져있는지 체크. set은 집합이었다...자료구조 다시해....
import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline


def diff(blue, red):
    global ans
    b_sum = r_sum = 0
    b_sum = sum(map(lambda x: places[x], blue))
    r_sum = sum(map(lambda x: places[x], red))

    # ans = min(ans, abs(b_sum-r_sum))
    return min(ans, abs(b_sum-r_sum))


def is_connected(ls):
    visited = [0]*(n+1)
    visited[0] = visited[ls[0]] = 1
    q = deque([ls[0]])
    ls = set(ls)
    while q:
        node = q.popleft()
        for curr in adj_ls[node]:
            if not visited[curr] and node in ls:
                visited[curr] = 1
                q.append(curr)

    for l in ls:
        if visited[l] == 0:
            return False
    return True


def all_connected():
    for i in range(1, (n//2)+1):
        combi = list(combinations(list(range(1, n+1)), i))
        for blue in combi:
            tmp_v = [1]+[0]*n
            for b in blue:
                tmp_v[b] = 1
            b_conn = is_connected(blue)
            if b_conn:  # blue 연결
                red = []
                for i in range(n+1):
                    if not tmp_v[i]:
                        red.append(i)
                r_conn = is_connected(red)
                if r_conn:
                    ans = diff(blue, red)
            if ans == 0:
                return


n = int(input())
places = [0]+list(map(int, input().split()))
adj_ls = [[] for _ in range(n+1)]

for i in range(1, n+1):
    tmp = list(map(int, input().split()))
    adj_ls[i].extend(tmp[1:])
ans = 1001

visited = [1, 1]+[0]*(n-1)  # 연결되지 않은 경우도 체크해줘야하므로
q = deque([1])
tmp_ls = [1]  # 이어진 구역 담는 리스트
while q:
    node = q.popleft()
    for j in adj_ls[node]:
        if not visited[j]:
            visited[j] = 1
            q.append(j)
            tmp_ls.append(j)
if len(tmp_ls) == n:  # 다 이어진 경우
    all_connected()
else:
    red = []
    set_tmp_ls = set(tmp_ls)
    for i in range(1, n+1):
        if i not in set_tmp_ls:
            red.append(i)
    r_conn = is_connected(red)
    if r_conn:
        ans = diff(tmp_ls, red)

print(ans if ans != 1001 else -1)

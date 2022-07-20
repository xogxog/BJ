# 슬라이딩 윈도우
from collections import deque,defaultdict
import sys
input = sys.stdin.readline

# 접시수, 초밥 가짓수, 연속해서 먹는 접시 수, 쿠폰 번호
N,d,k,c = map(int,input().split())
sushi = [int(input()) for _ in range(N)]
eat_sushi = deque() # 현재 먹은 스시 리스트
# cnt_sushi = {}
cnt_sushi = defaultdict(int)

for i in range(k) :
    eat_sushi.append(sushi[i])
    cnt_sushi[sushi[i]] += 1
    # if sushi[i] not in cnt_sushi :
    #     cnt_sushi[sushi[i]] = 1
    # else :
    #     cnt_sushi[sushi[i]] += 1

now_cnt = len(cnt_sushi) # 현재 먹을 수 있는 스시 갯수
ans = now_cnt
# 쿠폰 스시 체크
if c not in cnt_sushi :
    ans += 1
for j in range(N-1):
    tmp = eat_sushi.popleft()
    cnt_sushi[tmp] -= 1

    if cnt_sushi[tmp] == 0 :
        now_cnt -= 1

    eat_sushi.append(sushi[(j+k) % N]) # 먹을 스시 추가
    cnt_sushi[eat_sushi[-1]] += 1
    if cnt_sushi[eat_sushi[-1]] == 1 :
        now_cnt += 1
    # if eat_sushi[-1] in cnt_sushi :
    #     cnt_sushi[eat_sushi[-1]] += 1
    #     if cnt_sushi[eat_sushi[-1]] == 1:
    #         now_cnt += 1
    # else :
    #     cnt_sushi[eat_sushi[-1]] = 1
    #     now_cnt += 1

    if cnt_sushi[c] == 0 :
        ans = max(now_cnt + 1, ans)

    else :
        ans = max(now_cnt, ans)

print(ans)

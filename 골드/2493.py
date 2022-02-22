# 1. 순차적으로 스택에 들어옴. 들어올때(?) 첫번째면, ans에 0 넣기
# 2. 가장 첫번째보다 작으면 들어옴 / 자기 앞에 것 보다 크고 첫번째보다 작거나 같으면 들어옴.
# or 자신이 첫번째보다
import sys
n = int(input())
ls = list(map(int,sys.stdin.readline().split()))
s=0
ans =[0]
for i in range(1,n) :
    if i == s+1 and ls[i] < ls[s] :
        ans += [s + 1]
        # print(111111, s, ans)
    elif i > s+1 and ls[i-1] < ls[i] <= ls[s]: # s에 맞닿는 경우
        ans += [s + 1]
        # print(111111, s, ans)
    elif ans[-1] == 0 and ls[i]>ls[i-1] : # 맞닿는 곳이 없는 경우
        s = i
        ans += [0]
        # print(22222,s, ans)
    else:
        if ls[i-1] >= ls[i] : # 자기 바로앞이 자신보다 크거나 같은 경우
            s = i-1
            ans += [s+1]
            # print(333333, s, ans)
        else : # 그렇지 않을 경우 i가 가장 높음
            s = i
            ans += [s+1] # 자기자신이 가장 높으므로 닿는곳 없음 !?
            # print(44444, s, ans)

print(' '.join(list(map(str,ans))))
# 1. 순차적으로 스택에 들어옴. 들어올때(?) 첫번째면, ans에 0 넣기
# 2. 가장 첫번째보다 작으면 들어옴 / 자기 앞에 것 보다 크고 첫번째보다 작거나 같으면 들어옴.
# or 자신이 첫번째보다

# 8
# 10 1 3 7 2 5 4 6
import sys
n = int(input())
ls = list(map(int,sys.stdin.readline().split()))





zero_point = [0]
s=0
ans =[0]
for i in range(1,n) :
    if i == s+1 and ls[i] < ls[s] : # s에 맞닿는 경우
        ans += [s + 1]
        # print(000000, s, ans)
    elif i > s+1 and ls[i-1] < ls[i] < ls[s]: # s에 맞닿는 경우
        ans += [s + 1]
        # print(111111, s, ans)
    elif ans[-1] == 0 and ls[i]>ls[i-1] : # 맞닿는 곳이 없는 경우
        zero_point += [i]
        s = i
        ans += [0]
        # print(22222,s, ans)
    else:
        if ls[i-1] > ls[i] : # 자기 바로앞이 자신보다 크거나 같은 경우
            s = i-1
            ans += [s+1]
            zero_point += [i-1]
            # print(333333, s, ans)
        else : # 그렇지 않을 경우 i가 가장 높음
            s = i
            for j in range(len(zero_point)-1,-1,-1) :
                if ls[zero_point[j]] >= ls[i] : # 닿는곳있으면 .. 추가하자..!
                    ans += [zero_point[j]+1]
                    zero_point += [i]
                    break
            else :
                ans += [0]
                zero_point += [i]
            # print(44444, s, ans)

print(' '.join(list(map(str,ans))))


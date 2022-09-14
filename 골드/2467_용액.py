import sys
input = sys.stdin.readline
N = int(input())
ls = list(map(int,input().split()))

_min = 2000000001
l = 0
r = len(ls)-1

ans = (l,r)

while l<r :
    tmp_sum = ls[r]+ls[l]
    if abs(tmp_sum) < _min :
        _min = abs(tmp_sum)
        ans = (l,r)
    if tmp_sum == 0 :
        ans = (l,r)
        break
    elif tmp_sum < 0 :
        l += 1
    else :
        r -= 1


print(ls[ans[0]],ls[ans[1]])
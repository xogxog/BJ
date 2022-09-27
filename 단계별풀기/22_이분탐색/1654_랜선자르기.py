import sys
input = sys.stdin.readline

K,N = map(int,input().split())
ls = [int(input()) for _ in range (K)]
start ,end = 1, max(ls) # 자르는 단위 1부터 시작!
ans = 0

while start<=end :
    cnt = 0
    mid = (end+start)//2 # 난,,바보다,,
    for i in ls :
        cnt += i//mid
    if cnt < N :
        end = mid - 1
    else :
        start = mid + 1
        ans = max(ans,mid) # ans = mid로 해도 무방. -> cnt가 계속 많아지는 경우에만 이 조건문에 들어오기 때문에

print(ans)

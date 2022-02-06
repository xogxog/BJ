# 스위핑
# 한 쪽 방향부터 시작해서 다른 방향으로 스캔해가면서 쓸어가는 것
import sys

n = int(input())
ls = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)] # list 보다 tuple형태가 시간이 덜 걸린다!
ls.sort() # 스위핑은 정렬이 필요
ans = 0
start , end = ls[0]
for i in range(1,n):
    if start <=ls[i][0] <= end :
        end = max(ls[i][1], end) # if문을 쓰는 것 보다 덜 걸림 .. !

    else :
        ans += (end-start)
        start ,end = ls[i][0], ls[i][1]
ans += (end-start)
print(ans)

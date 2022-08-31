# 모양이 같은 행이여야 켜진다고 할 수 있다.
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
ls = [list(input().rstrip()) for _ in range(N)]
K = int(input())
max_cnt = 0
for i in range(N):
    tmp_cnt = 0
    tmp = ls[i].count('0')
    if tmp > K : # K 개수가 더 작으면 불을 다 못켬
        continue
    else :
        if (tmp % 2 == 0 and K % 2 == 0) or (tmp % 2 and K % 2) :# 짝수개, 짝수 번 불켬
            tmp_cnt += 1
            for j in range(i+1,N):
                if ls[i] == ls[j] :
                    tmp_cnt += 1
    max_cnt = max(max_cnt, tmp_cnt)
print(max_cnt)
# dp
import sys
input = sys.stdin.readline
n,k = map(int,input().split())

ls = [(0,0)]+[tuple(map(int,input().split())) for _ in range(n)] # (무게,가치)
bag = [[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1) :
    for j in range(1,k+1):

        w,v = ls[i] # 무게, 가치
        if j-w < 0 :
            bag[i][j] = bag[i-1][j] # 가방에 물건을 넣을 수 없는 상황이기때문에 그대로 들고옴
        else : # 그 전단계(i-1)에서 현재를 고려하는상황.
            bag[i][j] = max(bag[i-1][j-w]+v, bag[i-1][j])

print(bag[-1][-1])
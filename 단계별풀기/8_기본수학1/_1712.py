# 런타임 진짜...ㅂㄷㅂㄷ
import sys
a, b, c = map(int, sys.stdin.readline().rstrip().split())
# a = 고정비용
# b = 가변비용
# c = 노트북가격



if (c-b) <= 0 :
    print(-1)
else :
    n = a // (c - b)
    print(n+1)
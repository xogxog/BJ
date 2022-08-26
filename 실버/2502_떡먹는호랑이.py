# 첫째날 a
# 둘째날 b
# 각각 점화식으로 a,b의 상수를 구해 준 후, a값과 b값을 구한다.
import sys
input = sys.stdin.readline
def dduck() :
    for i in range(1, (k // aa) + 1):
        tmp_b = (k-(aa*i))
        if tmp_b % bb == 0 and tmp_b // bb >= i:
            print(i)
            print(tmp_b // bb)
            return

d,k = map(int,input().split()) #할머니가 넘어온 날, 호랑이에게 준 떡의 개수
ls_a = [0,1,0,1]
ls_b = [0,0,1,1]

for i in range(3,d):
    ls_a.append(ls_a[i]+ls_a[i-1])
    ls_b.append(ls_b[i]+ls_b[i-1])
aa = ls_a[-1]
bb = ls_b[-1]

dduck()


